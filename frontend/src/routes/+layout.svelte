<div class="page-block">
	<header class="header">
		<nav class="navbar">
			<div class="logo-block">
				<img class="logo-image" src="logo.png" alt="SubMaster Logo" />
				<span class="project-name">SubMaster</span>
			</div>

			<ul class="navlinks"></ul>

			<div class="call-to-action">
				<a class="sgn-in-btn" href="/sign-in-page">Войти</a>
				<a class="sgn-up-btn" href="/sign-up-page">Зарегистрироваться</a>
			</div>
		</nav>
	</header>

	<div class="slot-container">
		<slot></slot>
	</div>

	<footer class="footer">©SubMaster, Москва. Все права защищены</footer>
</div>

<style lang="scss">
	.page-block {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
	}

	.header {
		padding: 24px 80px;
	}

	.navbar {
		width: 1280px;
		height: 41px;

		display: flex;
		flex-direction: row;
		gap: 0 32px;

		.logo-block {
			display: flex;
			gap: 0 12px;

			width: 172px;
			height: 36px;

			.logo-image {
				width: 32px;
				height: 32px;

				margin-top: 4px;
			}

			.project-name {
				width: 126px;
				height: 25px;

				padding: 9px 1px 2px 0;

				font-size: 25px;
				font-weight: 600;
				color: #111928;
			}
		}

		.navlinks {
			width: 801px;
			height: 24px;

			margin: 8.5px 0;
		}

		.call-to-action {
			width: 244px;
			height: 41px;

			display: flex;
			gap: 0 16px;
            
            a {
				text-decoration: none;
			}

			.sgn-in-btn {
				width: 41px;
				height: 21px;

				margin: 11px 0 9px 0;
				padding: 0;

				border-style: none;
				background-color: transparent;

				font-size: 15px;
				font-weight: 500;
				color: #111928;
			}

			.sgn-up-btn {
				width: 186px;
				height: 15px;

				padding: 13px 20px 13px 20px;

				border-style: none;
				border-radius: 8px;

				background-color: #1a56db;

				font-size: 15px;
				font-weight: 500;
				color: #ffffff;
			}
		}
	}

	.slot-container {
		flex: 1;
	}

	.footer {
		font-size: 18.5px;
		font-weight: 400;
		color: #6b7280;

		padding: 4px 0 49.5px 76.13px;
	}
</style>
