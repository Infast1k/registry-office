<script>
	import { goto } from '$app/navigation';
	import { check_email, check_password, equals_password } from '$lib/scripts/form-validate.js';
	import axios from 'axios';

	let email = '';
	let password1 = '';
	let password2 = '';

	let valid_email = true;
	let valid_password = true;
	let equals_passwords = true;

	let show_password = false;

	let error = '';

	function validate() {
		valid_email = check_email(email);
		valid_password = check_password(password1);
		equals_passwords = equals_password(password1, password2);

		if (valid_email && valid_password && equals_passwords) {
			axios
				.post('http://localhost:8000/api/v1/auth/users/', {
					email: email,
					password: password1
				})
				.then((res) => {
					goto('/login');
				})
				.catch((err) => {
					error = 'Данная почта уже используется!';
					email = '';
					password1 = '';
					password2 = '';
					valid_email = false;
					valid_password = false;
					equals_passwords = false;
				});
		}

		if (!valid_email) {
			email = '';
		}
		if (!valid_password) {
			password1 = '';
			password2 = '';
		}
		if (!equals_passwords) {
			password2 = '';
		}
	}
</script>

<main>
	<div class="container">
		<div class="forms">
			<div class="form login">
				<div class="title-block">
					<span class="title">Регистрация</span>
				</div>
				{#if error}
					<div class="error-block">
						<span class="error">{error}</span>
					</div>
				{/if}
				<form action="#">
					<div class="input-field email-field">
						<input
							type="text"
							class={valid_email ? '' : 'invalid'}
							placeholder={valid_email ? 'Введите почту' : 'Некорректная почта'}
							bind:value={email}
							required
						/>
						<i class="uil uil-envelope icon" />
					</div>
					<div class="input-field">
						{#if show_password}
							<input
								type="text"
								placeholder={valid_password ? 'Введите пароль' : 'Некорректный пароль'}
								class={valid_password ? '' : 'invalid'}
								bind:value={password1}
								required
							/>
							<i class="uil uil-lock icon" />
						{:else}
							<input
								type="password"
								placeholder={valid_password ? 'Введите пароль' : 'Некорректный пароль'}
								class={valid_password ? '' : 'invalid'}
								bind:value={password1}
								required
							/>
							<i class="uil uil-lock icon" />
						{/if}
					</div>
					<div class="input-field">
						{#if show_password}
							<input
								type="text"
								placeholder={equals_passwords ? 'Подтвердите пароль' : 'Некорректный пароль'}
								class={equals_passwords ? '' : 'invalid'}
								bind:value={password2}
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
								placeholder={equals_passwords ? 'Подтвердите пароль' : 'Некорректный пароль'}
								class={equals_passwords ? '' : 'invalid'}
								bind:value={password2}
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
						<input type="button" value="Зарегистрироваться" on:click={validate} />
					</div>
				</form>
				<div class="login-signup">
					<span class="text"
						>Уже есть аккаунт?
						<a href="/login" class="text signup-text">Войти</a>
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
		background-color: var(--primary-color);
	}

	.container {
		position: relative;
		max-width: 700px;
		width: 300px;
		widows: 100%;
		background: #fff;
		box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
		border-radius: 10px;
	}

	.title-block {
		text-align: center;
	}

	.error-block {
		text-align: center;
		margin-top: 25px;
		border: 1px solid red;
		border-radius: 50px;
	}

	.error-block .error {
		font-weight: 500;
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
		background-color: var(--primary-color);
		border-radius: 25px;
	}

	.input-field {
		position: relative;
		height: 50px;
		width: 100%;
		margin-top: 30px;
	}

	.email-field {
		margin-top: 25px;
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
		border-bottom-color: var(--primary-color);
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
		color: var(--primary-color);
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
		color: var(--primary-color);
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
		background-color: var(--primary-color);
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
