let correctEstimationDirection = 'up'; // 全局变量，'up' 或 'down'
let currentScore = 0; // 初始积分
let countdownInterval = null;
let countdownTime = 8; // 倒计时时间（秒）
let isPaused = false;

// 初始化 Fireworks 实例
let fireworksInstance = null;

document.addEventListener('DOMContentLoaded', function() {
    setupGame();
    document.getElementById('calculate-button').addEventListener('click', calculate);
    document.getElementById('pause-button').addEventListener('click', togglePause);

    // 为估算按钮添加事件监听
    document.getElementById('toys').addEventListener('click', function(event) {
        if (event.target.tagName === 'BUTTON') {
            const direction = event.target.classList.contains('estimate-up') ? 'up' : 'down';
            const price = parseInt(event.target.getAttribute('data-price'));
            estimate(event.target, price, direction);
        }
    });
});

function setupGame() {
    const basePrices = [101, 112, 123, 134, 145, 119]; // 确保所有的价格都需要估算
    const toys = [
        { name: "玩具熊", basePrice: basePrices[Math.floor(Math.random() * basePrices.length)] },
        { name: "玩具车", basePrice: basePrices[Math.floor(Math.random() * basePrices.length)] }
    ];

    // 计算两个玩具的价格总和
    const totalBasePrice = toys.reduce((sum, toy) => sum + toy.basePrice, 0);

    const toysContainer = document.getElementById('toys');
    toysContainer.innerHTML = '';

    const money = Math.floor(Math.random() * 301) + 100; // 随机生成100到400之间的金额
    document.getElementById('money').textContent = money;

    // 决定正确的估计方向
    correctEstimationDirection = money > totalBasePrice ? 'up' : 'down';

    // 获取游戏容器和指令提示容器
    const gameContainer = document.getElementById('game');
    let instructionContainer = document.getElementById('instruction-container');

    if (!instructionContainer) {
        // 如果指令提示容器不存在，创建它
        instructionContainer = document.createElement('div');
        instructionContainer.id = 'instruction-container';

        // 创建灯泡图标（使用图片）
        const lightbulb = document.createElement('img');
        lightbulb.id = 'lightbulb';
        lightbulb.src = 'images/lightbulb.png'; // 确保有 lightbulb.png
        lightbulb.alt = '提示';
        lightbulb.width = 30;
        lightbulb.height = 30;
        lightbulb.style.cursor = 'pointer';

        // 创建提示内容
        const instruction = document.createElement('div');
        instruction.id = 'instruction';
        instruction.style.display = 'none'; // 初始状态隐藏

        // 将灯泡和提示内容添加到容器中
        instructionContainer.appendChild(lightbulb);
        instructionContainer.appendChild(instruction);

        // 将指令提示容器插入到游戏容器中，在 toysContainer 之前
        gameContainer.insertBefore(instructionContainer, toysContainer);
    }

    // 更新提示内容
    const instruction = instructionContainer.querySelector('#instruction');
    instruction.textContent = `因为钱包的钱 ${correctEstimationDirection === 'up' ? '>' : '<'} 玩具熊 + 玩具车，所以正确的估计方向是“向${correctEstimationDirection === 'up' ? '上' : '下'}估计”。`;

    // 初始化提示内容为隐藏
    instruction.style.display = 'none';

    // 获取灯泡图标元素
    const lightbulb = instructionContainer.querySelector('#lightbulb');

    // 为灯泡图标添加或更新点击事件监听器
    lightbulb.onclick = function() {
        const instruction = instructionContainer.querySelector('#instruction');
        if (instruction.style.display === 'none' || instruction.style.display === '') {
            instruction.style.display = 'block';
        } else {
            instruction.style.display = 'none';
        }
    };

    // 添加玩具元素
    toys.forEach(toy => {
        const price = toy.basePrice;
        const toyElement = document.createElement('div');
        toyElement.className = 'toy';

        // 映射玩具名称到图片路径
        let imagePath = '';
        if (toy.name === "玩具熊") {
            imagePath = 'images/bear.gif';
        } else if (toy.name === "玩具车") {
            imagePath = 'images/car.gif';
        } else {
            imagePath = 'images/default.gif'; // 默认图片路径
        }

        toyElement.innerHTML = `
            <img src="${imagePath}" alt="${toy.name}">
            <div class="details">
                <span class="name">${toy.name}</span>
                <span class="price">基础价格: ${price} 元</span>
                <button class="estimate-up" data-price="${price}">向上估计</button>
                <button class="estimate-down" data-price="${price}">向下估计</button>
                <span class="estimated"></span>
                <span class="feedback"></span>
            </div>
        `;
        toysContainer.appendChild(toyElement);
    });

    // 启用计算按钮
    const calculateButton = document.getElementById('calculate-button');
    calculateButton.disabled = false;

    // 清除之前的结果
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = '';
    resultDiv.classList.remove('correct', 'error');

    // 清除之前的估算和反馈
    const estimatedElements = document.querySelectorAll('.estimated');
    estimatedElements.forEach(elem => {
        elem.textContent = '';
        elem.removeAttribute('data-value');
        elem.removeAttribute('data-direction');
    });

    const feedbackElements = document.querySelectorAll('.feedback');
    feedbackElements.forEach(elem => {
        elem.textContent = '';
        elem.style.color = '';
    });

    // 隐藏倒计时容器
    const countdownContainer = document.getElementById('countdown-container');
    countdownContainer.classList.add('hidden');
    document.getElementById('countdown').textContent = countdownTime;
    isPaused = false;

    // 如果有正在运行的倒计时，清除它
    if (countdownInterval) {
        clearInterval(countdownInterval);
        countdownInterval = null;
    }
}



function estimate(buttonElement, price, direction) {
    const estimatedElement = buttonElement.parentNode.querySelector('.estimated');
    const feedbackElement = buttonElement.parentNode.querySelector('.feedback');

    // 根据方向进行估算
    let roundedPrice;
    if (direction === 'up') {
        roundedPrice = Math.ceil(price / 10) * 10;
    } else {
        roundedPrice = Math.floor(price / 10) * 10;
    }

    estimatedElement.textContent = `估计值：${roundedPrice} 元`;
    estimatedElement.setAttribute('data-value', roundedPrice);
    estimatedElement.setAttribute('data-direction', direction);

    // 验证当前估算是否符合全局应该的方向
    if (direction === correctEstimationDirection) {
        feedbackElement.textContent = '正确！';
        feedbackElement.style.color = 'green';
    } else {
        feedbackElement.textContent = '错误！';
        feedbackElement.style.color = 'red';
    }
}

function calculate() {
    const estimates = document.querySelectorAll('.estimated');
    let allEstimated = true;
    let allCorrect = true; // 标记所有估算是否正确

    estimates.forEach((estimate) => {
        const value = parseInt(estimate.getAttribute('data-value'));
        const direction = estimate.getAttribute('data-direction');
        const feedback = estimate.parentNode.querySelector('.feedback').textContent;

        if (isNaN(value)) {
            allEstimated = false;
        }

        if (feedback !== '正确！') {
            allCorrect = false;
        }
    });

    if (!allEstimated) {
        displayResult('请完成所有玩具的估算！', false);
        return;
    }

    // 如果所有估算都正确，则结果正确；否则，结果错误
    if (allCorrect) {
        displayResult('正确！', true);
        currentScore += 10;
        triggerFireworks(); // 触发烟花效果
    } else {
        displayResult('错误！', false);
        currentScore -= 10;
    }

    // 更新积分显示
    document.getElementById('current-score').textContent = currentScore;

    // 禁用计算按钮，防止多次点击
    const calculateButton = document.getElementById('calculate-button');
    calculateButton.disabled = true;

    // 开始倒计时
    startCountdown();
}

function displayResult(message, isCorrect) {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = message;
    if (isCorrect) {
        resultDiv.classList.remove('error');
        resultDiv.classList.add('correct');
    } else {
        resultDiv.classList.remove('correct');
        resultDiv.classList.add('error');
    }
}

function startCountdown() {
    let timeLeft = countdownTime;
    const countdownElement = document.getElementById('countdown');
    const countdownContainer = document.getElementById('countdown-container');
    countdownContainer.classList.remove('hidden');
    countdownElement.textContent = timeLeft;

    countdownInterval = setInterval(() => {
        if (!isPaused) {
            timeLeft--;
            if (timeLeft <= 0) {
                clearInterval(countdownInterval);
                countdownInterval = null;
                setupGame();
            }
            countdownElement.textContent = timeLeft;
        }
    }, 1000);
}

function togglePause() {
    isPaused = !isPaused;
    const pauseButton = document.getElementById('pause-button');
    pauseButton.textContent = isPaused ? '继续' : '暂停';
}

function triggerFireworks() {
    console.log('Triggering fireworks...');
    const canvas = document.getElementById('fireworks-canvas');

    if (!fireworksInstance) {
        try {
            fireworksInstance = new Fireworks(canvas, {
                hue: { min: 0, max: 360 },
                delay: { min: 15, max: 30 },
                rocketsPoint: 50,
                speed: 2,
                acceleration: 1.05,
                friction: 0.97,
                gravity: 1.5,
                particles: 50,
                trace: 3,
                explosion: 5,
                autoresize: true,
                brightness: { min: 50, max: 80 },
                opacity: 0.5,
            });
            fireworksInstance.start();
            console.log('Fireworks started');
        } catch (e) {
            console.error("Failed to initialize fireworks:", e);
            return;
        }
    } else {
        fireworksInstance.start();
        console.log('Fireworks restarted');
    }

    setTimeout(() => {
        if (fireworksInstance) {
            fireworksInstance.stop();
            console.log('Fireworks stopped');
        }
    }, 3000);
}