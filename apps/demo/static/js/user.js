function bind_modify_event(form_id) {
	$("#upProfile").bind("click", function () {
		$("#"+form_id).submit();
	});
	$("#clProfile").bind("click", function () {
		$("#"+form_id).form("reset");
	});
}

function bind_pwdchange_event(form_id) {
	$("#pwdChange").bind("click", function () {
		$("#"+form_id).submit();
	});
} 