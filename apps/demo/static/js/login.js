function bind_login_event() {
    $("#login").bind("click", function () {
        $("#loginForm").submit();
    });
    $("#cancel").bind("click", function () {
        $("#loginForm").form("reset");
    });
}
