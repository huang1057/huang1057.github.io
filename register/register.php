<?php
// 开启会话
session_start();

// 连接数据库
$host = 'mysql.sqlpub.com'; // 或者是你的数据库服务器地址
$dbname = 'campusweb';
$dbUsername = 'adminhuang'; // 根据你的数据库用户名进行替换
$dbPassword = '2C7YSumEaZzax3K8'; // 根据你的数据库密码进行替换

// 创建PDO实例
try {
    $pdo = new PDO("mysql:host=$host;dbname=$dbname;charset=utf8mb4", $dbUsername, $dbPassword, [
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
    ]);
} catch (PDOException $e) {
    die("数据库连接失败: " . $e->getMessage());
}

// 处理注册
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 从POST请求中获取数据
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';
    $email = $_POST['email'] ?? '';
    $user_type = $_POST['user_type'] ?? 'student'; // 默认用户类型为学生

    // 验证输入
    if (empty($username) || empty($password) || empty($email)) {
        $_SESSION['error'] = '所有字段都是必填项。';
        header('Location: register.html');
        exit();
    }

    // 检查用户名是否已存在
    $stmt = $pdo->prepare("SELECT username FROM users WHERE username = :username");
    $stmt->execute(['username' => $username]);
    if ($stmt->fetch()) {
        $_SESSION['error'] = '用户名已存在。';
        header('Location: register.html');
        exit();
    }

    // 密码加密
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // 插入新用户
    $sql = "INSERT INTO users (username, password, email, user_type) VALUES (?, ?, ?, ?)";
    $stmt = $pdo->prepare($sql);
    $stmt->execute([$username, $hashedPassword, $email, $user_type]);

    // 注册成功后重定向或显示消息
    $_SESSION['message'] = '注册成功，请登录。';
    header('Location: login.html');
    exit();
}
?>
