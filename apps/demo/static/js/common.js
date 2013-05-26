function bind_event_to_form(form_id, target_url, redirect_url) {
    $("#"+form_id).form({
        url: target_url,
        onSubmit: function () {
            var isValid = $(this).form("validate");
            return isValid;
        },
        success: function (data) {
            data = $.evalJSON(data);
            if (tools.show_message(data)) {
                if (redirect_url != undefined) {
                    document.location = redirect_url;
                }
            }
        }
    });
}