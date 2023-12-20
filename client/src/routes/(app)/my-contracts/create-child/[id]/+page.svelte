<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';

	export let data;

	let last_name = '';
	let first_name = '';
	let patronymic = '';
	let birth_date = '';
	let sex = '';
	let address = '';
	let place_of_birth = '';
	let vital = '';

	function is_empty(last_name, first_name, birth_date, address, sex, place_of_birth, vital) {
		if (!last_name || !first_name || !birth_date || !address || !sex || !place_of_birth || !vital) {
			return true;
		}
		return false;
	}

	function create_contract() {
		if (
			is_empty(last_name, first_name, patronymic, birth_date, address, sex, place_of_birth, vital)
		) {
			alert('Все поля обязательны для заполнения!');
			return;
		}
		const child_data = {
			last_name: last_name,
			first_name: first_name,
			patronymic: patronymic,
			birth_date: birth_date,
			address: address,
			sex: sex,
			status: sex == 'мужчина' ? 'сын' : 'дочь',
			place_of_birth: place_of_birth,
			vital_record: vital
		};

		axios
			.post(`http://localhost:8000/api/v1/weddings/children/${data.slug}/`, child_data, {
				headers: {
					Authorization: `Token ${get(token)}`
				}
			})
			.then((res) => {
				goto(`/my-contracts/${data.slug}`);
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

			<label for="birth-date">Дата рождения</label>
			<input type="date" id="birth-date" name="birth-date" bind:value={birth_date} />

			<label for="status">Пол</label>
			<select id="sex" name="sex" bind:value={sex}>
				<option value="мужчина">Мужчина</option>
				<option value="женщина">Женщина</option>
			</select>

			<label for="address">Адрес проживания</label>
			<input
				type="text"
				id="address"
				name="address"
				placeholder="Адрес проживания.."
				bind:value={address}
			/>

			<label for="place_of_birth">Место рождения</label>
			<input
				type="text"
				id="place_of_birth"
				name="place_of_birth"
				placeholder="Место рождения.."
				bind:value={place_of_birth}
			/>

			<label for="vital">Код регистрации</label>
			<input
				type="text"
				id="vital"
				name="vital"
				placeholder="Код регистрации.."
				bind:value={vital}
			/>

			<div class="submit">
				<input type="button" value="Добавить ребенка" on:click={create_contract} />
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
