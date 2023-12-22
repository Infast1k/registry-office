<script>
	import { goto } from '$app/navigation';
	import image from '$lib/images/default_image.jpg';

	export let data;
	let user = data.user;
</script>

<div class="container">
	<div class="card-container">
		<img class="round" src={image} width="150" alt="user" />
		<h3>{user.profile.last_name} {user.profile.first_name} {user.profile.patronymic}</h3>
		<h6>Почта: {user.email}</h6>
		<h6>Телефон: {user.profile.phone}</h6>
		<h6>Дата рождения: {user.profile.birth_date}</h6>
		<h6>
			Серия, номер паспорта: {user.profile.passport.series} - {user.profile.passport.numbers}
		</h6>
		<h6>Дата выдачи паспорта: {user.profile.passport.created_at}</h6>
		<h6>Кем выдан: {user.profile.passport.registration_place}</h6>
		<h6>Адрес: {user.profile.address}</h6>
		<div class="buttons">
			<button
				class="primary ghost"
				on:click={() => {
					goto('/');
				}}
			>
				На главную
			</button>
		</div>
	</div>
</div>

<style>
	.card-container {
		margin: 0 auto;
		margin-top: 7%;
		padding-bottom: 50px;
	}

	* {
		box-sizing: border-box;
	}

	h3 {
		margin: 10px 0;
	}

	h6 {
		margin: 5px 0;
		text-transform: uppercase;
	}

	.card-container {
		background-color: #231e39;
		border-radius: 5px;
		box-shadow: 0px 10px 20px -10px rgba(0, 0, 0, 0.75);
		color: #b3b8cd;
		padding-top: 30px;
		position: relative;
		width: 350px;
		max-width: 100%;
		text-align: center;
	}

	.card-container .round {
		border: 1px solid #03bfcb;
		border-radius: 50%;
		padding: 7px;
	}

	button.primary {
		background-color: #03bfcb;
		border: 1px solid #03bfcb;
		border-radius: 3px;
		color: #231e39;
		font-family: Montserrat, sans-serif;
		font-weight: 500;
		padding: 10px 25px;
	}

	button.primary.ghost {
		margin-top: 60px;
		background-color: transparent;
		color: #02899c;
		cursor: pointer;
	}
	button.primary.ghost:hover {
		background-color: #03bfcb;
		border: 1px solid #03bfcb;
		border-radius: 3px;
		color: #231e39;
		font-family: Montserrat, sans-serif;
		font-weight: 500;
		padding: 10px 25px;
		cursor: pointer;
	}
</style>
