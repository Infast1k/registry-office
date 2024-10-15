<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';

	export let data;

	let last_name = '';
	let first_name = '';
	let patronymic = '';
	let phone = '';
	let birth_date = '';
	let address = '';

	function is_empty(last_name, first_name, patronymic, phone, birth_date, address) {
		if (!last_name || !first_name || !patronymic || !phone || !birth_date || !address) {
			return true;
		}
		return false;
	}

	function create_witness() {
		if (is_empty(last_name, first_name, patronymic, phone, birth_date, address)) {
			alert('Все поля обязательны для заполнения!');
			return;
		}

		const user = {
			last_name: last_name,
			first_name: first_name,
			patronymic: patronymic,
			phone: phone,
			birth_date: birth_date,
			address: address
		};

		axios
			.post(`http://localhost:8000/api/v1/weddings/witnesses/${data.slug}/`, user, {
				headers: {
					Authorization: `Token ${get(token)}`
				}
			})
			.then((res) => {
				goto(`/my-contracts/${data.slug}/`);
				return;
			})
			.catch((errors) => {
				alert(errors.response.data.error);
			});
	}
</script>

<div class="container">
	<div class="form-container">
		<form>
			<label for="lname">Фамилия</label>
			<input
				type="text"
				id="lname"
				name="lastname"
				placeholder="Фамилия.."
				bind:value={last_name}
			/>

			<label for="fname">Имя</label>
			<input type="text" id="fname" name="firstname" placeholder="Имя.." bind:value={first_name} />

			<label for="patronymic">Отчество</label>
			<input
				type="text"
				id="patronymic"
				name="patronymic"
				placeholder="Отчество.."
				bind:value={patronymic}
			/>

			<label for="phone">Телефон</label>
			<input type="tel" id="phone" name="phone" placeholder="Номер телефона.." bind:value={phone} />

			<label for="birth-date">Дата рождения</label>
			<input type="date" id="birth-date" name="birth-date" bind:value={birth_date} />

			<label for="address">Адрес проживания</label>
			<input
				type="text"
				id="address"
				name="address"
				placeholder="г. Город, ул. Улица, д. дом, кв. Kвартира"
				bind:value={address}
			/>

			<div class="submit">
				<input type="button" value="Добавить свидетеля" on:click={create_witness} />
			</div>
		</form>
	</div>
</div>

<style>
	* {
		background: var(--body-color);
	}
	.form-container {
		width: 60%;
		margin: 0 auto;
		text-align: center;
	}

	input[type='text'],
	input[type='date'],
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
		width: 30%;
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
