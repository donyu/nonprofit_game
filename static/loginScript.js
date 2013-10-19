$(function() {
	$('#loginForm').submit(function(event) {
		$.ajax({
			data: JSON.stringify({
				username: $('#username').val(),
				password: $('#password').val()
			}),
			url: '/login',
			contentType: 'application/json;charset=UTF-8',
			type: 'POST',
			success: function(response) {
				window.location.replace('/');
			}
		});
		event.preventDefault();
	});

	$('#registerForm').submit(function(event) {
		$.ajax({
			data: JSON.stringify({
				username: $('#registerUsername').val(),
				password: $('#registerPassword').val(),
				email: $('#registerEmail').val()
			}),
			url: '/register',
			contentType: 'application/json;charset=UTF-8',		
			type: 'POST',
			success: function(response) {
				window.location.replace('/');
			}
		});
		event.preventDefault();
	});
});