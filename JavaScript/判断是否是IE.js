		// 检测是否为IE
		function isIe() {
			var i = navigator.userAgent.toLowerCase().indexOf("msie");
			return i >= 0;
		}
		if (isIe() == "false") {
			url = "IE.html";
			location.href = url;
		};