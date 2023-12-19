<script>
	export let data;
	let users = data.users;
</script>

<div class="container">
	<h1>Список пользователей</h1>
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
				{#each users as user (user.id)}
					<tr>
						<td
							>{user.profile.last_name}
							{user.profile.first_name}
							{user.profile.patronymic}</td
						>
						<td>{user.profile.phone}</td>
						<td>{user.profile.birth_date}</td>
						<td>{user.profile.address}</td>
						<td>{user.role.role_name}</td>
						<td><button on:click={() => {}}>редактировать</button></td>
						<td><button on:click={() => {}}>удалить</button></td>
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
