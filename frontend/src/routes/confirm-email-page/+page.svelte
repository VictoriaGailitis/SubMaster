<main class="main">
	<img
		class="illustration"
		src="static/man-character-wave.png"
		alt="Мужчина приветственно машет рукой"
	/>

	<div class="confirmation-form">
		<h2>Зарегистрироваться в SubMaster</h2>

		<label for="email">Электронная почта</label>
		<div class="input-group">
			<input type="email" id="email" placeholder="name@flowbite.com" disabled />
		</div>

		<label for="code">Код подтверждения</label>
		<div class="code-input-group">
			<input type="text" placeholder="•" maxlength="1" />
			<input type="text" placeholder="•" maxlength="1" />
			<input type="text" placeholder="•" maxlength="1" />
			<input type="text" placeholder="•" maxlength="1" />
			<input type="text" placeholder="•" maxlength="1" />
			<input type="text" placeholder="•" maxlength="1" />
		</div>

		<button type="button" class="confirm-button">Подтвердить</button>
	</div>
</main>

<style lang="scss">
	.main {
		margin: 55.5px 125px 55.5px 0;
		display: flex;
		flex-direction: row;
		align-items: center;

		.confirmation-form {
			width: 563px;
			height: 339px;
			background-color: #ffffff;
			padding: 32px;
			border-radius: 10px;
			box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);

			h2 {
				font-size: 24px;
				margin-bottom: 20px;
				color: #333;
			}

			label {
				font-size: 14px;
				color: #555;
				margin-bottom: 8px;
				display: block;
			}

			.input-group input {
				width: 100%;
				padding: 12px;
				border: 1px solid #ddd;
				border-radius: 5px;
				margin-bottom: 20px;
				font-size: 16px;
				color: #333;
			}

			.code-input-group {
				display: flex;
				gap: 10px;
				margin-bottom: 20px;

				input {
					width: 50px;
					height: 50px;
					text-align: center;
					font-size: 24px;
					border: 1px solid #ddd;
					border-radius: 5px;
				}

                input::placeholder {
                    text-align: center;
                }
			}

			.confirm-button {
				width: 100%;
				padding: 12px;
				font-size: 16px;
				background-color: #1a56db;
				color: #fff;
				border: none;
				border-radius: 5px;
				cursor: pointer;
				transition: background-color 0.3s;

				&:hover {
					background-color: #0056b3;
				}
			}
		}
	}

	.illustration {
		width: 752px;
		height: 752px;
	}
</style>
