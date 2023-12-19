<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';

	export let data;

	let last_name = data.relative.last_name;
	let phone = data.relative.phone;
	let address = data.relative.address;

	function is_empty(last_name, phone, address) {
		if (!last_name || !phone || !address) {
			return true;
		}
		return false;
	}

	function save_changes() {
		if (is_empty(last_name, phone, address)) {
			alert('Все поля обязательны для заполнения!');
			return;
		}

		const user_data = {
			last_name: last_name,
			phone: phone,
			address: address
		};

		axios
			.put(`http://localhost:8000/api/v1/relatives/${data.slug}/`, user_data, {
				headers: {
					Authorization: `Token ${get(token)}`
				}
			})
			.then((res) => {
				goto('/relatives');
				return;
			})
			.catch((errors) => {
				console.log(errors);
			});
	}
</script>

<div class="container">
	<h1>Редактирвоание профиля</h1>
	<div>
		<form>
			<label for="lname">Фамилия</label>
			<input
				type="text"
				id="lname"
				name="lastname"
				placeholder="Фамилия.."
				bind:value={last_name}
			/>

			<label for="phone">Телефон</label>
			<input type="tel" id="phone" name="phone" placeholder="Номер телефона.." bind:value={phone} />

			<label for="address">Адрес проживания</label>
			<input
				type="text"
				id="address"
				name="address"
				placeholder="г. Город, ул. Улица, д. дом, кв. Kвартира"
				bind:value={address}
			/>

			<div class="submit">
				<input type="button" value="Сохранить изменения" on:click={save_changes} />
			</div>
		</form>
	</div>
</div>

<style>
	.container {
		text-align: center;
	}
	.submit {
		margin: 0;
		padding: 0;
		text-align: center;
	}

	input[type='text'],
	input[type='tel'] {
		width: 100%;
		padding: 12px 20px;
		margin: 8px 0;
		display: inline-block;
		border: 1px solid #ccc;
		border-radius: 4px;
		box-sizing: border-box;
	}

	input[type='button'] {
		width: 20%;
		background-color: #4caf50;
		color: white;
		padding: 14px 20px;
		margin: 8px 0;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	input[type='button']:hover {
		background-color: #45a049;
	}

	div {
		padding: 10px 5px 10px 5px;
	}
</style>
