$(function() {
	$('#loginForm').submit(function(event) {
		$.ajax({
			data: {
				username: $('#username').val(),
				password: $('#password').val()
			},
			url: '/login',
			type: 'POST',
			success: function(response) {
				window.location.replace('/');
			}
		});
		event.preventDefault();
	});

	$('#registerForm').submit(funtion(event) {
		$.ajax({
			data: {
				username: $('#registerUsername').val(),
				password: $('#registerPassword').val(),
				email: $('#registerEmail').val()
			},
			url: '/register',
			type: 'POST',
			success: function(response) {
				window.location.replace('/');
			}
		});
		event.preventDefault();
	});
});