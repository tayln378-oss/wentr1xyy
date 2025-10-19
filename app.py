from flask import Flask, render_template_string

app = Flask(__name__)

# КАТЕГОРИИ И ТОВАРЫ - настраивай здесь!
CATEGORIES = {
    "кламси": {
        "telegram_link": "https://t.me/mangosuperedit",
        "items": [
            {"name": "Мое кламси", "price": "0$", "image": "🦪", "description": "Телепортирует вас и вы не видны для проивника!", "product_link": "https://t.me/c/2286228615/1037"},
            {"name": "Пока-что нет", "price": "0$", "image": "👑", "description": "-", "product_link": ""},
            {"name": "Пока-что нет", "price": "0$", "image": "🛠️", "description": "-", "product_link": ""}
        ]
    },
    "кфг": {
        "telegram_link": "https://t.me/mangosuperedit", 
        "items": [
            {"name": "Кофиги", "price": "0$", "image": "🎯", "description": "Для метро", "product_link": "https://t.me/c/2286228615/871"},
            {"name": "Visual CFG", "price": "0$", "image": "👁️", "description": "Визуальные настройки", "product_link": "https://t.me/c/2286228615/871"},
            {"name": "Performance Pack", "price": "0$", "image": "⚡", "description": "Оптимизация производительности", "product_link": "https://t.me/c/2286228615/871"}
        ]
    },
    "читы": {
        "telegram_link": "https://t.me/mangosuperedit",
        "items": [
            {"name": "Wallhack", "price": "0$", "image": "👻", "description": "Очень хорошиий чит в вх", "product_link": "https://t.me/c/2286228615/871"},
            {"name": "Aimbot", "price": "0$", "image": "🤖", "description": "Топовый аим", "product_link": "https://t.me/c/2286228615/871"},
            {"name": "ESP Pack", "price": "0$", "image": "📡", "description": "Все сразу", "product_link": "https://t.me/c/2286228615/871"}
        ]
    }
}

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>wentr1xystore - Лучшие продукты</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            --bg-secondary: rgba(255, 255, 255, 0.95);
            --text-primary: #333;
            --text-secondary: #666;
            --text-white: white;
            --accent-color: #667eea;
            --shadow: 0 10px 30px rgba(0,0,0,0.1);
            --card-bg: rgba(255, 255, 255, 0.95);
        }

        .dark-theme {
            --bg-primary: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            --bg-secondary: rgba(30, 30, 46, 0.95);
            --text-primary: #ffffff;
            --text-secondary: #b0b0b0;
            --text-white: white;
            --accent-color: #7e6fff;
            --shadow: 0 10px 30px rgba(0,0,0,0.3);
            --card-bg: rgba(40, 40, 60, 0.95);
        }

        body {
            font-family: 'Arial', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            min-height: 100vh;
            transition: all 0.3s ease;
        }

        .navbar {
            background: var(--bg-secondary);
            padding: 1rem 0;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            box-shadow: var(--shadow);
            backdrop-filter: blur(10px);
        }

        .nav-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            background: linear-gradient(45deg, var(--accent-color), #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .nav-right {
            display: flex;
            gap: 1rem;
            align-items: center;
        }

        .theme-toggle {
            background: none;
            border: 2px solid var(--accent-color);
            color: var(--accent-color);
            padding: 8px 15px;
            border-radius: 20px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .theme-toggle:hover {
            background: var(--accent-color);
            color: white;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--text-primary);
            font-weight: 500;
            transition: color 0.3s;
        }

        .nav-links a:hover {
            color: var(--accent-color);
        }

        .hero {
            margin-top: 80px;
            text-align: center;
            padding: 6rem 2rem;
            color: var(--text-white);
        }

        .hero h1 {
            font-size: 3.5rem;
            margin-bottom: 1rem;
            opacity: 0;
            animation: fadeInUp 1s ease 0.2s forwards;
        }

        .hero p {
            font-size: 1.3rem;
            margin-bottom: 2rem;
            opacity: 0;
            animation: fadeInUp 1s ease 0.5s forwards;
        }

        .categories {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .category-card {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 2.5rem;
            text-align: center;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeInUp 0.6s ease forwards;
            cursor: pointer;
            color: var(--text-primary);
        }

        .category-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        }

        .category-icon {
            font-size: 4rem;
            margin-bottom: 1rem;
            display: block;
        }

        .category-name {
            font-size: 1.8rem;
            font-weight: bold;
            margin-bottom: 1rem;
            color: var(--text-primary);
        }

        .category-description {
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            line-height: 1.5;
        }

        .items-grid {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }

        .item-card {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 2rem;
            text-align: center;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(30px);
            animation: fadeInUp 0.6s ease forwards;
            color: var(--text-primary);
        }

        .item-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }

        .item-image {
            font-size: 3rem;
            margin-bottom: 1rem;
            display: block;
        }

        .item-name {
            font-size: 1.3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
            color: var(--text-primary);
        }

        .item-price {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--accent-color);
            margin-bottom: 1rem;
        }

        .item-description {
            color: var(--text-secondary);
            margin-bottom: 1.5rem;
            line-height: 1.5;
            font-size: 0.9rem;
        }

        .btn {
            background: linear-gradient(45deg, var(--accent-color), #764ba2);
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }

        .btn:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        .btn-download {
            background: linear-gradient(45deg, #00b894, #00a085);
        }

        .btn-telegram {
            background: linear-gradient(45deg, #0088cc, #00a2ff);
        }

        .btn-secondary {
            background: transparent;
            border: 2px solid var(--accent-color);
            color: var(--accent-color);
        }

        .btn-secondary:hover {
            background: var(--accent-color);
            color: white;
        }

        .back-btn {
            margin: 2rem auto;
            text-align: center;
        }

        .footer {
            background: rgba(0, 0, 0, 0.8);
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 4rem;
        }

        .contact-telegram {
            margin: 1rem 0;
            font-size: 1.1rem;
        }

        .contact-telegram a {
            color: #0088cc;
            text-decoration: none;
            font-weight: bold;
        }

        /* Анимации */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }

        .pulse {
            animation: pulse 2s infinite;
        }

        /* Задержки для анимаций */
        .category-card:nth-child(1) { animation-delay: 0.1s; }
        .category-card:nth-child(2) { animation-delay: 0.2s; }
        .category-card:nth-child(3) { animation-delay: 0.3s; }

        .hidden {
            display: none;
        }

        /* Адаптивность */
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2.5rem;
            }
            
            .nav-links {
                gap: 1rem;
            }
            
            .categories, .items-grid {
                padding: 1rem;
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <!-- Навигация -->
    <nav class="navbar">
        <div class="nav-container">
            <div class="logo">wentr1xystore</div>
            <div class="nav-right">
                <div class="nav-links">
                    <a href="#" onclick="showCategories()">Категории</a>
                    <a href="#contact">Контакты</a>
                </div>
                <button class="theme-toggle" onclick="toggleTheme()">🌙 Тема</button>
            </div>
        </div>
    </nav>

    <!-- Главная страница с категориями -->
    <div id="categories-page">
        <section class="hero">
            <h1>🛒 wentr1xystore</h1>
            <p>Лучшие продукты для софтеров от @mangosuperedit</p>
            <a href="#categories" class="btn pulse">Выбрать категорию</a>
        </section>

        <section class="categories" id="categories">
            <div class="category-card" onclick="showCategory('кламси')">
                <div class="category-icon">🦪</div>
                <h3 class="category-name">Кламси</h3>
                <p class="category-description">Качественные кламси для различных игр</p>
                <div class="btn">Выбрать</div>
            </div>

            <div class="category-card" onclick="showCategory('кфг')">
                <div class="category-icon">⚙️</div>
                <h3 class="category-name">КФГ</h3>
                <p class="category-description">Оптимальные конфигурации для игр</p>
                <div class="btn">Выбрать</div>
            </div>

            <div class="category-card" onclick="showCategory('читы')">
                <div class="category-icon">🎮</div>
                <h3 class="category-name">Читы</h3>
                <p class="category-description">Топовые читы для победы в играх</p>
                <div class="btn">Выбрать</div>
            </div>
        </section>
    </div>

    <!-- Страница товаров категории -->
    <div id="category-page" class="hidden">
        <section class="hero">
            <h1 id="category-title">Товары</h1>
            <p id="category-subtitle">Выберите нужный товар</p>
            <div class="back-btn">
                <button class="btn btn-secondary" onclick="showCategories()">← Назад к категориям</button>
            </div>
        </section>

        <section class="items-grid" id="items-container">
            <!-- Товары будут добавляться через JavaScript -->
        </section>

        <section class="hero">
            <div class="contact-telegram">
                <p>💬 По вопросам пишите в Telegram:</p>
                <a href="https://t.me/mangosuperedit" class="btn btn-telegram">@mangosuperedit</a>
            </div>
        </section>
    </div>

    <!-- Футер -->
    <footer class="footer" id="contact">
        <p>© 2024 wentr1xystore. Все права защищены.</p>
        <div class="contact-telegram">
            <p>Связь через Telegram: <a href="https://t.me/mangosuperedit">@mangosuperedit</a></p>
        </div>
    </footer>

    <script>
        const categories = {{ categories|tojson }};

        // Переключение темы
        function toggleTheme() {
            document.body.classList.toggle('dark-theme');
            const themeBtn = document.querySelector('.theme-toggle');
            themeBtn.textContent = document.body.classList.contains('dark-theme') ? '☀️ Тема' : '🌙 Тема';
            
            // Сохраняем тему в localStorage
            localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? 'dark' : 'light');
        }

        // Загрузка сохраненной темы
        function loadTheme() {
            const savedTheme = localStorage.getItem('theme');
            if (savedTheme === 'dark') {
                document.body.classList.add('dark-theme');
                document.querySelector('.theme-toggle').textContent = '☀️ Тема';
            }
        }

        function showCategories() {
            document.getElementById('categories-page').classList.remove('hidden');
            document.getElementById('category-page').classList.add('hidden');
        }

        function showCategory(categoryName) {
            const category = categories[categoryName];
            
            // Обновляем заголовок
            document.getElementById('category-title').textContent = categoryName;
            document.getElementById('category-subtitle').textContent = `Товары в категории "${categoryName}"`;
            
            // Очищаем и добавляем товары
            const itemsContainer = document.getElementById('items-container');
            itemsContainer.innerHTML = '';
            
            category.items.forEach((item, index) => {
                const itemCard = document.createElement('div');
                itemCard.className = 'item-card';
                itemCard.style.animationDelay = `${index * 0.1}s`;
                
                // Создаем кнопку скачивания только если есть ссылка
                let buttonHtml = '';
                if (item.product_link && item.product_link.trim() !== '') {
                    buttonHtml = `<a href="${item.product_link}" target="_blank" class="btn btn-download">📥 Скачать</a>`;
                }
                // Если ссылки нет - кнопки не будет вообще
                
                itemCard.innerHTML = `
                    <div class="item-image">${item.image}</div>
                    <h3 class="item-name">${item.name}</h3>
                    <div class="item-price">${item.price}</div>
                    <p class="item-description">${item.description}</p>
                    ${buttonHtml}
                `;
                itemsContainer.appendChild(itemCard);
            });
            
            // Показываем страницу категории
            document.getElementById('categories-page').classList.add('hidden');
            document.getElementById('category-page').classList.remove('hidden');
            
            // Прокрутка вверх
            window.scrollTo(0, 0);
        }

        // Плавная прокрутка для навигации
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Загружаем тему при старте
        loadTheme();
    </script>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, categories=CATEGORIES)

if __name__ == '__main__':
    print("🛒 wentr1xystore запущен!")
    print("👉 Открой: http://localhost:5000")
    print("💡 Чтобы изменить категории и товары, редактируй CATEGORIES в коде")
    app.run(debug=True)