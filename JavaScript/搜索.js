function search() {
				// 获取搜索框内容
				var text = document.getElementById("searchs").value;
				if (text == "") {
					// 防止跳转至必应首页
					alert("未输入文字");
				} else {
					url = "/getpy?text=" + text
					$.get(url, function(data) {
						window.location.href = '/data/' + data;
					})
				}
			}