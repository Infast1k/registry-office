<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';

	let last_name = '';
	let first_name = '';
	let patronymic = '';
	let phone = '';
	let birth_date = '';
	let address = '';
	let sex = '';
	let series = '';
	let number = '';
	let created_at = '';
	let registration_place = '';
	let change_sex = false;
	let event_datetime = '';

	function is_empty(
		last_name,
		first_name,
		phone,
		birth_date,
		address,
		sex,
		series,
		number,
		created_at,
		registration_place
	) {
		if (
			!last_name ||
			!first_name ||
			!phone ||
			!birth_date ||
			!address ||
			!sex ||
			!series ||
			!number ||
			!created_at ||
			!registration_place
		) {
			return true;
		}
		return false;
	}

	function create_contract() {
		if (
			is_empty(
				last_name,
				first_name,
				phone,
				birth_date,
				address,
				sex,
				series,
				number,
				created_at,
				registration_place
			)
		) {
			alert('Все поля обязательны для заполнения!');
			return;
		}
		const contract_data = {
			last_name: last_name,
			first_name: first_name,
			patronymic: patronymic,
			phone: phone,
			birth_date: birth_date,
			address: address,
			sex: sex,
			series: series,
			numbers: number,
			created_at: created_at,
			registration_place: registration_place,
			change_last_name: change_sex,
			event_datetime: event_datetime
		};

		axios
			.post('http://localhost:8000/api/v1/weddings/', contract_data, {
				headers: {
					Authorization: `Token ${get(token)}`
				}
			})
			.then((res) => {
				goto('/my-contracts/');
				return;
			})
			.catch((errors) => {
				alert(errors.response.data.error);
				console.log(errors);
			});
	}
</script>

<div class="container">
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

			<label for="series">Серия паспорта</label>
			<input type="text" id="series" name="series" bind:value={series} />

			<label for="number">Номер паспорта</label>
			<input type="text" id="number" name="number" bind:value={number} />

			<label for="registration_place">Паспорт выдан</label>
			<input
				type="text"
				id="registration_place"
				name="registration_place"
				bind:value={registration_place}
			/>

			<label for="created_at">Дата выдачи</label>
			<input type="date" id="created_at" name="created_at" bind:value={created_at} />

			<label for="address">Адрес проживания</label>
			<input
				type="text"
				id="address"
				name="address"
				placeholder="г. Город, ул. Улица, д. дом, кв. Kвартира"
				bind:value={address}
			/>

			<label for="status">Пол</label>
			<select id="sex" name="sex" bind:value={sex}>
				<option value="мужчина">Мужчина</option>
				<option value="женщина">Женщина</option>
			</select>

			<label for="change_sex">Сменить фамилию партнерше</label>
			<input type="checkbox" name="change_sex" id="change_sex" bind:checked={change_sex} />

			<br />

			<label for="event_datetime">Время проведения мероприятия</label>
			<input
				type="datetime-local"
				id="event_datetime"
				name="event_datetime"
				min="2023-01-01T00:00"
				max="2026-12-01T00:00"
				bind:value={event_datetime}
			/>

			<div class="submit">
				<input type="button" value="Создать договор" on:click={create_contract} />
			</div>
		</form>
	</div>
</div>

<style>
	.submit {
		margin: 0;
		padding: 0;
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
