/** Create reCAPTCHA-protected mailto: links.
 *
 * Prerequisites
 * -------------
 * The reCAPTCHA Javascript must be included in the page.
 * Each mail link must have a data-mailkey attribute.
 * This is automatically done by the "mailhide" template tag for Django.
 * The code also require the g_recaptcha element to exist; it is also handled automatically by the "mailhide" template tag.
 */
var mailhide = mailhide || {
    /** Actual URL that will return the e-mail address after checking the reCAPTCHA challenge */
    RESULT_URL: 'mailhide/api/v1/mail',
    /** The element that triggered the reCAPTCHA challenge */
    REQUESTED_ELEMENT: null,
    /** Flag to indicate we're waiting for a reply from the reCAPTCHA code */
    REQUEST_PENDING: false,
    /** Add their behavior to an <a> tag.
     *
     * The tag is available through "this".
     */
    initA: function() {
        var jqElem = $(this);
        jqElem.on('click', (e) => {
            e.preventDefault();
            if (mailhide.REQUEST_PENDING) {
                return;
            }
            mailhide.REQUEST_PENDING = true;
            mailhide.REQUESTED_ELEMENT = jqElem;
            grecaptcha.execute();
        });
    },
    /** Initialize all appropriate <a> tags */
    init: function() {
        $('a[data-mailkey]').each(mailhide.initA);
    }
};
/** Callback called by reCAPTCHA when the challenge complete */
function mailhide_cb(response_token) {
    var mailkey = mailhide.REQUESTED_ELEMENT.data('mailkey');
    var data = {
        'response': response_token,
        'key': mailkey
    };
    var result = $.getJSON(
        mailhide.RESULT_URL,
        data,
        (reply) => {
            if (reply.meta.total_count != 1) {
                return;
            }
            var address = reply.objects[0].address;
            var subject = mailhide.REQUESTED_ELEMENT.data('subject');
            var link = 'mailto:' + address;
            if (subject) {
                link += '?subject=' + subject.replace(/&/g, '%26');
            }
            mailhide.REQUEST_PENDING = false;
            window.location.href = link;
        });
}
$(mailhide.init);
