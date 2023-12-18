<script>
	import { token } from '$lib/stores/userStore.js';
	import { get } from 'svelte/store';

	export let data;
	let relatives = data.relatives;

	function example() {
		// Срабатывает при добавлении нового родственника
	}
</script>

<div class="container">
	<h1>Родственники</h1>
	<button on:click={example}>Добавить родственника</button>
	<div class="tbl-header">
		<table cellpadding="0" cellspacing="0" border="0">
			<thead>
				<tr>
					<th>ФИО</th>
					<th>Телефон</th>
					<th>Дата рождения</th>
					<th>Адрес</th>
					<th>Статус</th>
					<th />
					<th />
				</tr>
			</thead>
		</table>
	</div>
	<div class="tbl-content">
		<table cellpadding="0" cellspacing="0" border="0">
			<tbody>
				{#each relatives as relative (relative.id)}
					<tr>
						<td
							>{relative.abstract_profile.last_name}
							{relative.abstract_profile.first_name}
							{relative.abstract_profile.patronymic}</td
						>
						<td>{relative.abstract_profile.phone}</td>
						<td>{relative.abstract_profile.birth_date}</td>
						<td>{relative.abstract_profile.address}</td>
						<td>{relative.status.status_name}</td>
						<td><button>редактировать</button></td>
						<td
							><button
								on:click={() => {
									fetch(`http://localhost:8000/api/v1/relatives/${relative.id}/`, {
										method: 'DELETE',
										headers: {
											Authorization: `Token ${get(token)}`
										}
									});
									location.reload();
								}}>удалить</button
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
