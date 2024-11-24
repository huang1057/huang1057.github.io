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

// 处理登录
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // 从POST请求中获取用户名和密码
    $username = $_POST['username'] ?? '';
    $password = $_POST['password'] ?? '';

    // 验证用户名和密码是否被填写
    if (empty($username) || empty($password)) {
        $_SESSION['error'] = '用户名和密码都是必填项。';
        header('Location: login.html');
        exit();
    }

    // 预处理SQL语句以防止SQL注入
    $stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username");
    $stmt->bindParam(':username', $username);
    $stmt->execute();

    // 获取用户数据
    $user = $stmt->fetch();

    // 检查用户是否存在以及密码是否正确
    if ($user && password_verify($password, $user['password'])) {
        // 密码正确，创建会话
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['username'];
        $_SESSION['user_type'] = $user['user_type'];

        // 根据用户类型重定向到不同的页面
        if ($user['user_type'] === 'admin') {
            header('Location: ../admin/index.html');
        } else {
            header('Location: ../index.html');
        }
        exit();
    } else {
        // 用户名或密码错误
        $_SESSION['error'] = '无效的用户名或密码。';
        header('Location: login.html');
        exit();
    }
}
?>

