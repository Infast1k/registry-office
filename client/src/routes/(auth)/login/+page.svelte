<script>
	import { goto } from '$app/navigation';
	import { check_email, check_password } from '$lib/scripts/form-validate.js';

	let email = '';
	let password = '';

	let invalid_email = false;
	let invalid_password = false;

	let show_password = false;

	function validate() {
		var valid_email = check_email(email);
		var valid_password = check_password(password);

		if (valid_email && valid_password) {
			// Функция авторизации
			// Обработка ответа с сервера
			// Сохранение токена в store
			goto('/profile');
			return;
		}

		email = '';
		password = '';
		invalid_email = true;
		invalid_password = true;
	}
</script>

<main>
	<div class="container">
		<div class="forms">
			<div class="form login">
				<div class="title-block">
					<span class="title">Авторизация</span>
				</div>
				<form action="#">
					<div class="input-field">
						<input
							type="text"
							class={invalid_email ? 'invalid' : ''}
							placeholder={invalid_email ? 'Некорректная почта' : 'Введите почту'}
							bind:value={email}
							required
						/>
						<i class="uil uil-envelope icon" />
					</div>
					<div class="input-field">
						{#if show_password}
							<input
								type="text"
								placeholder={invalid_password ? 'Некорректный пароль' : 'Введите пароль'}
								class={invalid_password ? 'invalid' : ''}
								bind:value={password}
								required
							/>
							<i class="uil uil-lock icon" />
							<!-- svelte-ignore a11y-click-events-have-key-events -->
							<!-- svelte-ignore a11y-no-static-element-interactions -->
							<i
								class="uil uil-eye-slash showHidePw"
								on:click={() => {
									show_password = !show_password;
								}}
							/>
						{:else}
							<input
								type="password"
								placeholder={invalid_password ? 'Некорректный пароль' : 'Введите пароль'}
								class={invalid_password ? 'invalid' : ''}
								bind:value={password}
								required
							/>
							<i class="uil uil-lock icon" />
							<!-- svelte-ignore a11y-click-events-have-key-events -->
							<!-- svelte-ignore a11y-no-static-element-interactions -->
							<i
								class="uil uil-eye-slash showHidePw"
								on:click={() => {
									show_password = !show_password;
								}}
							/>
						{/if}
					</div>
					<div class="input-field button">
						<input type="button" value="Войти" on:click={validate} />
					</div>
				</form>
				<div class="login-signup">
					<span class="text"
						>Нет аккаунта?
						<a href="/register" class="text signup-text">Зарегистрироваться</a>
					</span>
					<span class="text back-to-home">
						<a href="/" class="text signup-text">Вернуться на главную</a>
					</span>
				</div>
			</div>
		</div>
	</div>
</main>

<style>
	main {
		height: 100vh;
		display: flex;
		align-items: center;
		justify-content: center;
		background-color: #4070f4;
	}

	.container {
		position: relative;
		max-width: 430px;
		widows: 100%;
		background: #fff;
		box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
	}

	.title-block {
		text-align: center;
	}

	.form {
		padding: 30px;
	}
	.title {
		position: relative;
		font-size: 27px;
		font-weight: 600;
	}

	.title::before {
		content: '';
		position: absolute;
		left: 0;
		bottom: 0;
		height: 3px;
		width: 40px;
		background-color: #4070f4;
		border-radius: 25px;
	}

	.input-field {
		position: relative;
		height: 50px;
		width: 100%;
		margin-top: 30px;
	}

	.input-field input {
		position: absolute;
		height: 100%;
		width: 100%;
		padding: 0 35px;
		border: none;
		outline: none;
		font-size: 16px;
		border-bottom: 2px solid #ccc;
		border-top: 2px solid transparent;
		transition: all 0.2s ease;
	}

	.input-field input:is(:focus, :valid) {
		border-bottom-color: #4070f4;
	}

	.input-field input.invalid {
		border-bottom-color: red;
	}

	.input-field i {
		position: absolute;
		top: 50%;
		transform: translateY(-50%);
		color: #999;
		font-size: 23px;
		transition: all 0.2s ease;
		cursor: pointer;
	}

	.input-field input:is(:focus, :valid) ~ i {
		color: #4070f4;
	}

	.icon {
		left: 0;
	}

	.showHidePw {
		right: 0;
	}

	.form .text {
		color: #333;
		font-size: 14px;
	}

	.form a.text {
		color: #4070f4;
		text-decoration: none;
	}

	.form a:hover {
		text-decoration: underline;
	}

	.form .button {
		margin-top: 35px;
	}

	.form .button input {
		border: none;
		color: #fff;
		font-size: 17px;
		font-weight: 500;
		letter-spacing: 1px;
		border-radius: 6px;
		background-color: #4070f4;
		cursor: pointer;
		transition: all 0.3s ease;
	}

	.button input:hover {
		background-color: #265df2;
	}

	.form .login-signup {
		display: flex;
		flex-direction: column;
		margin-top: 20px;
		text-align: center;
	}

	.back-to-home {
		margin-top: 10px;
	}
</style>
