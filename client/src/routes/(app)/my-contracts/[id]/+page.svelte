<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';

	import { goto } from '$app/navigation';

	export let data;
	let contract = data.contract;
	let witnesses = data.witnesses;
</script>

<h3>
	{#if contract.user.profile.sex == 'мужчина'}
		ФИО мужа:
	{:else}
		ФИО жены:
	{/if}
	{contract.user.profile.last_name}
	{contract.user.profile.first_name}
	{contract.user.profile.patronymic}
</h3>

<h3>Телефон: {contract.user.profile.phone}</h3>
<h3>Дата рождения: {contract.user.profile.birth_date}</h3>
<h3>
	Серия - номер паспорта: {contract.user.profile.passport.series} - {contract.user.profile.passport
		.numbers}
</h3>
<h3>Адрес проживания: {contract.user.profile.address}</h3>

<br />

<h3>
	{#if contract.profile.sex == 'мужчина'}
		ФИО мужа:
	{:else}
		ФИО жены:
	{/if}
	{contract.profile.last_name}
	{contract.profile.first_name}
	{contract.profile.patronymic}
</h3>
<h3>Телефон: {contract.profile.phone}</h3>
<h3>Дата рождения: {contract.profile.birth_date}</h3>
<h3>
	Серия - номер паспорта: {contract.profile.passport.series} - {contract.profile.passport.numbers}
</h3>
<h3>Адрес проживания: {contract.profile.address}</h3>

<h1>Свидетили</h1>
<div class="tbl-header">
	<table cellpadding="0" cellspacing="0" border="0">
		<thead>
			<tr>
				<th>ФИО</th>
				<th>Телефон</th>
				<th>Дата рождения</th>
				<th>Адрес</th>
				<th />
			</tr>
		</thead>
	</table>
</div>
<div class="tbl-content">
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
					<td
						><button
							on:click={() => {
								console.log(witness.witness.id);

								axios
									.delete(`http://localhost:8000/api/v1/weddings/witnesses/${witness.id}/`, {
										headers: {
											Authorization: `Token ${get(token)}`
										}
									})
									.then((res) => {})
									.catch((errors) => {
										alert(errors.response.data.error);
										console.log(errors);
									});
								// Обновляем страницу
								location.reload();
							}}>удалить</button
						></td
					>
				</tr>
			{/each}
		</tbody>
	</table>
</div>
<button
	on:click={() => {
		goto(`/my-contracts/create-witness/${data.slug}/`);
	}}>Добавить свидетеля</button
>

<h1>Дети</h1>

<style>
	h1 {
		font-size: 30px;
		color: black;
		text-transform: uppercase;
		font-weight: 600;
		text-align: center;
		margin-bottom: 15px;
	}
	table {
		margin: 0 auto;
		width: 50%;
		table-layout: fixed;
	}
	.tbl-header {
		background-color: rgba(255, 255, 255, 0.3);
	}
	.tbl-content {
		height: 300px;
		overflow-x: auto;
		margin-top: 0px;
		border: 1px solid rgba(255, 255, 255, 0.3);
	}
	th {
		padding: 20px 15px;
		text-align: left;
		font-weight: 500;
		font-size: 14px;
		color: black;
		text-transform: uppercase;
	}
	td {
		padding: 15px;
		text-align: left;
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
