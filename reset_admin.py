{% extends "base.html" %}
{% block content %}
<div class="main-container">
    <div class="card">
        <h3><i class="fas fa-user-plus"></i> Add New Teacher</h3>
        <form action="/add_teacher" method="POST" class="grid-form">
            <input type="text" name="n" placeholder="Full Name" required>
            <input type="text" name="u" placeholder="Username" required>
            <input type="password" name="p" placeholder="Password" required>
            <button type="submit" class="btn-reg">Save Teacher</button>
        </form>
    </div>

    <div class="card" style="margin-top:20px;">
        <h3><i class="fas fa-chalkboard-teacher"></i> Active Teacher List</h3>
        <table style="width:100%; border-collapse: collapse; margin-top: 10px;">
            <tr style="background:#3c4b9b; color:white;">
                <th style="padding: 12px; text-align: left;">Name</th>
                <th style="padding: 12px; text-align: left;">Username</th>
                <th style="padding: 12px; text-align: left;">Status</th>
                <th style="padding: 12px; text-align: center;">Actions</th>
            </tr>
            {% for t in teachers %}
            <tr style="border-bottom: 1px solid #eee;">
                <td style="padding: 12px;">{{ t.name }}</td>
                <td style="padding: 12px;">{{ t.username }}</td>
                <td style="padding: 12px;">
                    <span style="color: {{ 'green' if t.status == 'active' else 'red' }}; font-weight: bold;">
                        {{ t.status.upper() }}
                    </span>
                </td>
                <td style="padding: 12px; text-align: center;">
                    <a href="/toggle_teacher/{{ t.id }}" 
                       title="Change Status" 
                       style="color:#3c4b9b; font-size:22px; margin-right: 15px; text-decoration: none;">
                        <i class="fas fa-toggle-{{ 'on' if t.status == 'active' else 'off' }}"></i>
                    </a>

                    <a href="/delete_teacher/{{ t.id }}" 
                       title="Delete Teacher"
                       onclick="return confirm('Are you sure? This will also remove their timetable entries.')" 
                       style="color:#e74c3c; font-size:18px; text-decoration: none;">
                        <i class="fas fa-trash-alt"></i>
                    </a>
                </td>
            </tr>
            {% endfor %}
        </table>
    </div>
</div>

<style>
    .grid-form { display: grid; grid-template-columns: 1fr 1fr 1fr auto; gap: 10px; margin-top: 15px; }
    input { padding: 10px; border: 1px solid #ddd; border-radius: 4px; }
    .btn-reg { background: #3c4b9b; color: white; border: none; padding: 10px 20px; border-radius: 4px; cursor: pointer; font-weight: bold; }
    .btn-reg:hover { background: #2a356e; }
    tr:hover { background-color: #f9f9f9; }
</style>
{% endblock %}