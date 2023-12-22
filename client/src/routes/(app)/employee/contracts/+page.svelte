<script>
	import axios from 'axios';
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';
	import { goto } from '$app/navigation';

	export let data;
	let contracts = data.contracts;
</script>

<div class="container">
	<h1>Управление договорами</h1>
	<div class="tbl-header">
		<table cellpadding="0" cellspacing="0" border="0">
			<thead>
				<tr>
					<th>ФИО</th>
					<th>ФИО</th>
					<th>Дата проведения</th>
					<th>Статус</th>
					<th />
				</tr>
			</thead>
		</table>
	</div>
	<div class="tbl-content">
		<table cellpadding="0" cellspacing="0" border="0">
			<tbody>
				{#each contracts as contract (contract.id)}
					<tr>
						<td
							>{contract.user.profile.last_name}
							{contract.user.profile.first_name}
							{contract.user.profile.patronymic}</td
						>
						<td
							>{contract.profile.last_name}
							{contract.profile.first_name}
							{contract.profile.patronymic}</td
						>
						<td>{contract.event_datetime}</td>
						<td>{contract.status.status_name}</td>
						<td
							><button
								on:click={() => {
									goto(`/employee/contracts/${contract.id}/`);
								}}>Подробнее</button
							></td
						>
					</tr>
				{/each}
			</tbody>
		</table>
	</div>
</div>

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
		width: 90%;
		table-layout: fixed;
	}
	.tbl-header {
		background-color: rgba(255, 255, 255, 0.3);
	}
	.tbl-content {
		height: 400px;
		overflow-x: auto;
		margin-top: 0px;
		border: 1px solid rgba(255, 255, 255, 0.3);
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
