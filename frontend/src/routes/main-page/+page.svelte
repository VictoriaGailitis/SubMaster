<main class="main">
	<img
		class="illustration"
		src="static/girl-character-ok.png"
		alt="Девушка показывает жест &quot;Окей&quot;"
	/>

	<div class="description-container">
		<section class="description-section">
			<h2 class="heading">
				<img class="heading-icon" src="static/icons/eye.png" alt="Синяя иконка в форме глаза" />
				<span class="heading-text">Отслеживай</span>
			</h2>
			<p class="description-text">
				Все твои подписки, будь то российские или зарубежные, в одном удобном приложении.
			</p>
		</section>

		<section class="description-section">
			<h2 class="heading">
				<img
					class="heading-icon"
					src="static/icons/ordered-list.png"
					alt="Синяя иконка в форме нумерованного списка"
				/>
				<span class="heading-text">Управляй</span>
			</h2>
			<p class="description-text">
				Изменяй, отменяй, добавляй, покупай подписки - все в твоих руках.
			</p>
		</section>

		<section class="description-section">
			<h2 class="heading">
				<img
					class="heading-icon"
					src="static/icons/cash.png"
					alt="Синяя иконка в форме наличных денег"
				/>
				<span class="heading-text">Экономь</span>
			</h2>
			<p class="description-text">
				Получай уведомления о предстоящих платежах и отменяй ненужные подписки, чтобы не тратить
				деньги впустую.
			</p>
		</section>
	</div>
</main>

<style lang="scss">
	.main {
		margin: 122px 125px;

		display: flex;
		flex-direction: row;
		gap: 64px;
	}

	.illustration {
		width: 312px;
		height: 602px;
	}

	.description-container {
		width: 814px;
		height: 602px;

		display: flex;
		flex-direction: column;
		gap: 100px 0;

		.description-section {
			display: flex;
			flex-direction: column;
			gap: 20px 0;

			.heading {
				width: 293px;
				height: 54px;

				display: flex;
				flex-direction: row;
				gap: 0 14px;

				.heading-icon {
					width: 50px;
					height: 50px;

					margin: 2px 0;
				}

				.heading-text {
					margin: 7px 0;

					font-size: 38px;
					font-weight: 700;
					color: #1a56db;
				}
			}

			.description-text {
				font-size: 25.2px;
				font-weight: 400px;
				color: #000000;
				line-height: 36px;
			}
		}
	}
</style>
