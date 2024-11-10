<main class="main">
	<img
		class="illustration"
		src="static/man-character-wave.png"
		alt="Мужчина приветственно машет рукой"
	/>

	<div class="login-form-container">
		<h2>Войти в SubMaster</h2>
		<form class="login-form">
			<label for="email">Электронная почта</label>
			<div class="input-group">
				<span class="icon">📧</span>
				<input type="email" id="email" placeholder="name@flowbite.com" required />
			</div>
			<label for="password">Пароль</label>
			<input type="password" id="password" placeholder="●●●●●●●●" required />
			<div class="remember-me">
				<input type="checkbox" id="remember" />
				<label for="remember">Запомнить меня</label>
			</div>
			<button type="submit">Войти</button>
			<div class="form-footer">
				<a href="#">Забыли пароль?</a>
				<p>Не зарегистрированы? <a href="/sign-up-page">Создать аккаунт</a></p>
			</div>
		</form>
	</div>
</main>

<style lang="scss">
    .main {
		margin: 55.5px 125px 55.5px 0;
		display: flex;
		flex-direction: row;
		align-items: center;
	}

	.login-form-container {
		width: 563px;
		height: 427px;
		padding: 32px;
		border: 1px solid #e0e0e0;
		border-radius: 10px;
		box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);

		h2 {
			margin-bottom: 20px;
			font-size: 24px;
			color: #333;
		}

		.login-form {
			display: flex;
			flex-direction: column;

			label {
				font-size: 14px;
				color: #333;
				margin-bottom: 5px;
			}

			.input-group {
				display: flex;
				align-items: center;
				border: 1px solid #ccc;
				border-radius: 5px;
				padding: 10px;
				margin-bottom: 15px;

				.icon {
					margin-right: 8px;
					font-size: 18px;
					color: #888;
				}

				input {
					flex: 1;
					border: none;
					outline: none;
					font-size: 14px;
				}
			}

			input[type="password"] {
				border: 1px solid #ccc;
				border-radius: 5px;
				padding: 10px;
				margin-bottom: 15px;
				font-size: 14px;
			}

			.remember-me {
				display: flex;
				align-items: center;
				font-size: 14px;
				color: #333;
				margin-bottom: 15px;

				input {
					margin-right: 5px;
				}
			}

			button {
				background-color: #0056e0;
				color: #fff;
				border: none;
				padding: 12px;
				border-radius: 5px;
				cursor: pointer;
				font-size: 16px;
				margin-bottom: 10px;

				&:hover {
					background-color: #0041b5;
				}
			}

			.form-footer {
				text-align: center;
				font-size: 14px;

				a {
					color: #0056e0;
					text-decoration: none;

					&:hover {
						text-decoration: underline;
					}
				}

				p {
					margin-top: 10px;
				}
			}
		}
	}

	.illustration {
		width: 752px;
		height: 752px;
	}
</style>
