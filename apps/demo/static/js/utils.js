function Tools() {
    this.show_message = function (data) {
        if ("errmsg" in data) {
            $.messager.alert("错误信息", data.errmsg);
            return false;
        } else {
        	$.messager.alert("消息", data.msg);
        	return true;
        }
    }
}