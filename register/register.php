<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>用户注册 - 校园网</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>校园网</h1>
        <nav>
            <ul>
                <li><a href="index.php">首页</a></li>
                <li><a href="login.php">登录</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <h2>用户注册</h2>
        <form action="register_process.php" method="post">
            <input type="text" name="username" placeholder="用户名" required />
            <input type="password" name="password" placeholder="密码" required />
            <input type="email" name="email" placeholder="邮箱" required />
            <select name="role" required>
                <option value="student">学生</option>
                <option value="staff">教职员工</option>
            </select>
            <select name="class_id" required>
                <option value="">选择班级</option>
                <?php
                // 从数据库中获取班级
                $pdo = new PDO("sqlite:campusweb.db");
                $stmt = $pdo->query("SELECT * FROM Classes");
                while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
                    echo "<option value='{$row['class_id']}'>{$row['class_name']}</option>";
                }
                ?>
            </select>
            <input type="submit" value="注册" />
        </form>
    </main>

    <footer>
        <p>版权所有 &copy; 2024 校园网</p>
    </footer>
</body>
</html>
