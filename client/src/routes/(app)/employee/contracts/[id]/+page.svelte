<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';

	import { goto } from '$app/navigation';

	export let data;
	let contract = data.contract;
	let witnesses = data.witnesses;
	let children = data.children;

	let contract_status = contract.status.status_name;

	function is_empty(status) {
		return !status ? true : false;
	}

	function update_contract_status() {
		if (is_empty(contract_status)) {
			alert('Поле "Статус договора" не может быть пустым!');
			return;
		}
		const contract_data = {
			status: contract_status
		};

		axios
			.put(`http://localhost:8000/api/v1/employee/weddings/${data.slug}/`, contract_data, {
				headers: {
					Authorization: `Token ${get(token)}`
				}
			})
			.then((res) => {
				alert(`Статус успешно изменен на '${contract_data.status}'`);
			})
			.catch((errors) => {
				alert(errors.response.data.error);
			});
	}
</script>

<h1>Молодожены</h1>
<div class="tbl-header">
	<table cellpadding="0" cellspacing="0" border="0">
		<thead>
			<tr>
				<th>ФИО</th>
				<th>Телефон</th>
				<th>Дата рождения</th>
				<th>Серия номер паспорта</th>
				<th>Адрес</th>
				<th>Статус договора</th>
			</tr>
		</thead>
	</table>
</div>
<div class="tbl-content couple">
	<table cellpadding="0" cellspacing="0" border="0">
		<tbody>
			<tr>
				<td
					>{contract.profile.last_name}
					{contract.profile.first_name}
					{contract.profile.patronymic}</td
				>
				<td>{contract.profile.phone}</td>
				<td>{contract.profile.birth_date}</td>
				<td>{contract.profile.passport.series}-{contract.profile.passport.numbers}</td>
				<td>{contract.profile.address}</td>
				<td>
					<form action="">
						<select id="status" name="status" bind:value={contract_status}>
							<option value="На рассмотрении">На рассмотрении</option>
							<option value="В браке">В браке</option>
							<option value="В разводе">В разводе</option>
							<option value="Одобрен">Одобрен</option>
							<option value="В рассмотрении на развод">В рассмотрении на развод</option>
						</select>
					</form>
				</td>
			</tr>
			<tr>
				<td
					>{contract.user.profile.last_name}
					{contract.user.profile.first_name}
					{contract.user.profile.patronymic}</td
				>
				<td>{contract.user.profile.phone}</td>
				<td>{contract.user.profile.birth_date}</td>
				<td>{contract.user.profile.passport.series}-{contract.profile.passport.numbers}</td>
				<td>{contract.user.profile.address}</td>
				<td><button class="submit" on:click={update_contract_status}>Изменить статус</button></td>
			</tr>
		</tbody>
	</table>
</div>

<h1>Свидетили</h1>
<div class="tbl-header">
	<table cellpadding="0" cellspacing="0" border="0">
		<thead>
			<tr>
				<th>ФИО</th>
				<th>Телефон</th>
				<th>Дата рождения</th>
				<th>Адрес</th>
			</tr>
		</thead>
	</table>
</div>
<div class="tbl-content witnesses">
	<table cellpadding="0" cellspacing="0" border="0">
		<tbody>
			{#each witnesses as witness (witness.id)}
				<tr>
					<td
						>{witness.witness.last_name}
						{witness.witness.first_name}
						{witness.witness.patronymic}</td
					>
					<td>{witness.witness.phone}</td>
					<td>{witness.witness.birth_date}</td>
					<td>{witness.witness.address}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>

<h1 class="h1 witness-h1">Дети</h1>
<div class="tbl-header">
	<table cellpadding="0" cellspacing="0" border="0">
		<thead>
			<tr>
				<th>ФИО</th>
				<th>Дата рождения</th>
				<th>Место рождения</th>
				<th>Адрес</th>
			</tr>
		</thead>
	</table>
</div>
<div class="tbl-content children">
	<table cellpadding="0" cellspacing="0" border="0">
		<tbody>
			{#each children as child (child.id)}
				<tr>
					<td
						>{child.child.last_name}
						{child.child.first_name}
						{child.child.patronymic}</td
					>
					<td>{child.child.birth_date}</td>
					<td>{child.birth_sertificate.place_of_birth}</td>
					<td>{child.address}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</div>

<style>
	* {
		background: var(--body-color);
	}
	.submit {
		text-align: center;
	}
	h1 {
		font-size: 30px;
		color: black;
		text-transform: uppercase;
		font-weight: 600;
		text-align: center;
		margin-bottom: 15px;
	}

	.witness-h1 {
		margin-bottom: 0px;
	}

	select {
		width: 100%;
		padding: 5px 5px;
		margin: 8px 0;
		display: inline-block;
		border: 1px solid #ccc;
		border-radius: 4px;
		box-sizing: border-box;
	}

	table {
		margin: 0 auto;
		width: 90%;
		table-layout: fixed;
	}
	.tbl-content {
		overflow-x: auto;
		margin-top: 0px;
		border: 1px solid rgba(255, 255, 255, 0.3);
	}

	.tbl-content.couple {
		height: 200px;
	}

	.tbl-content.witnesses {
		height: 250px;
	}

	.tbl-content.children {
		height: 250px;
		padding-bottom: 100px;
	}

	th {
		padding: 20px 15px;
		text-align: center;
		font-weight: 500;
		font-size: 14px;
		color: black;
		text-transform: uppercase;
	}

	button {
		background-color: var(--primary-color);
		color: white;
		padding: 1px 2px;
		border: none;
		border-radius: 4px;
		cursor: pointer;
	}

	td {
		padding: 15px;
		text-align: center;
		vertical-align: middle;
		font-weight: 300;
		font-size: 12px;
		color: black;
		border-bottom: solid 1px rgba(255, 255, 255, 0.1);
	}

	/* скролл бар */

	::-webkit-scrollbar {
		width: 6px;
	}
	::-webkit-scrollbar-track {
		-webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
	}
	::-webkit-scrollbar-thumb {
		-webkit-box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.3);
	}
</style>
