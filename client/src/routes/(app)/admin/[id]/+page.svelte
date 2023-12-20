<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';

	export let data;
	let user = data.user;

	let role = user.role.role_name;
</script>

<div class="container">
	<div class="card-container">
		<img class="round" src="https://randomuser.me/api/portraits/women/79.jpg" alt="user" />
		<h3>{user.profile.last_name} {user.profile.first_name} {user.profile.patronymic}</h3>
		<h6>Телефон: {user.profile.phone}</h6>
		<h6>Дата рождения: {user.profile.birth_date}</h6>
		<h6>Адрес: {user.profile.address}</h6>
		<h6>Роль: {user.role.role_name}</h6>
		<div class="buttons">
			<select id="status" name="status" bind:value={role}>
				<option value="user">Пользователь (user)</option>
				<option value="employee">Сотрудник (employee)</option>
				<option value="admin">Администратор (admin)</option>
			</select>
			<br />
			<button
				class="primary"
				on:click={() => {
					const role_date = {
						role: role
					};
					axios
						.put('http://localhost:8000/api/v1/admin/users/4/', role_date, {
							headers: {
								Authorization: `Token ${get(token)}`
							}
						})
						.then((res) => {
							goto('/admin/');
							return;
						})
						.catch((errors) => {
							console.log(errors);
						});
				}}
			>
				Обновить роль
			</button>
			<br />
			<button
				class="primary ghost"
				on:click={() => {
					goto('/admin/');
				}}
			>
				Вернуться назад
			</button>
		</div>
	</div>
</div>

<style>
	.buttons select {
		margin-bottom: 7px;
		padding: 3px 33px;
		margin: 8px 0;
		display: inline-block;
		border: 1px solid #ccc;
		border-radius: 4px;
		box-sizing: border-box;
	}

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
	}
</style>
