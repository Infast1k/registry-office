<script>
	import { Fileupload, Label } from 'flowbite-svelte';
	import { goto } from '$app/navigation';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import axios from 'axios';

	let last_name = '';
	let first_name = '';
	let patronymic = '';
	let sex = '';
	let phone = '';
	let birth_date = '';
	let series = '';
	let numbers = '';
	let registration_place = '';
	let created_at = '';
	let address = '';
	let value;

	function is_empty() {
		if (
			!last_name ||
			!first_name ||
			!patronymic ||
			!sex ||
			!phone ||
			!birth_date ||
			!series ||
			!numbers ||
			!registration_place ||
			!created_at ||
			!address
		) {
			return true;
		}
		return false;
	}

	function create_profile() {
		if (is_empty()) {
			alert('Все поля обязательны для заполнения!');
			return;
		}
		const req_data = {
			last_name: last_name,
			first_name: first_name,
			patronymic: patronymic,
			sex: sex,
			birth_date: birth_date,
			phone: phone,
			address: address,
			image: value,
			numbers: numbers,
			series: series,
			registration_place: registration_place,
			created_at: created_at
		};

		axios
			.post('http://localhost:8000/api/v1/profile/', req_data, {
				headers: {
					Authorization: `Token ${get(token)}`
				}
			})
			.then((res) => {
				goto('/profile');
			})
			.catch((errors) => {
				console.log(errors);
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

			<label for="status">Пол</label>
			<select id="sex" name="sex" bind:value={sex}>
				<option value="мужчина">Мужчина</option>
				<option value="женщина">Женщина</option>
			</select>

			<label for="phone">Телефон</label>
			<input type="tel" id="phone" name="phone" placeholder="Номер телефона.." bind:value={phone} />

			<label for="birth-date">Дата рождения</label>
			<input type="date" id="birth-date" name="birth-date" bind:value={birth_date} />

			<label for="series">Серия паспорта</label>
			<input
				type="text"
				id="series"
				name="series"
				placeholder="Серия паспрта.."
				bind:value={series}
			/>

			<label for="number">Номер паспорта</label>
			<input
				type="text"
				id="number"
				name="number"
				placeholder="Номер паспорта.."
				bind:value={numbers}
			/>

			<label for="registration_place">Кем выдан</label>
			<input
				type="text"
				id="registration_place"
				name="registration_place"
				placeholder="Паспорт выдан.."
				bind:value={registration_place}
			/>

			<label for="created_at">Дата выдачи</label>
			<input
				type="date"
				id="created_at"
				name="created_at"
				placeholder="Дата выдачи паспорта.."
				bind:value={created_at}
			/>

			<label for="address">Адрес проживания</label>
			<input
				type="text"
				id="address"
				name="address"
				placeholder="г. Город, ул. Улица, д. дом, кв. Kвартира"
				bind:value={address}
			/>

			<!-- <Label for="with_helper" class="pb-2">Upload file</Label>
			<Fileupload id="with_helper" class="mb-2" bind:value /> -->
			<div class="submit">
				<input type="button" value="Создать профиль" on:click={create_profile} />
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
	input[type='tel'],
	input[type='date'],
	select {
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
