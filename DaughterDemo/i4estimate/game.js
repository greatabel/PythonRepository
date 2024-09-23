let correctEstimationDirection = 'up'; // 全局变量，'up' 或 'down'

document.addEventListener('DOMContentLoaded', function() {  
    setupGame();  
    document.getElementById('calculate-button').addEventListener('click', calculate);  

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

    // 添加指令提示
    const gameContainer = document.getElementById('game');
    const existingInstruction = document.getElementById('instruction');
    if (existingInstruction) {
        existingInstruction.remove();
    }
    const instruction = document.createElement('div');
    instruction.id = 'instruction';
    instruction.style.marginBottom = '10px';
    instruction.style.fontWeight = 'bold';
    instruction.style.color = 'blue';
    instruction.textContent = correctEstimationDirection === 'up' 
        ? '提示：正确的估计方向是“向上估计”。' 
        : '提示：正确的估计方向是“向下估计”。';
    gameContainer.insertBefore(instruction, toysContainer);

    toys.forEach(toy => {  
        const price = toy.basePrice;  
        const toyElement = document.createElement('div');  
        toyElement.className = 'toy';  
        toyElement.innerHTML = `  
            <span class="name">${toy.name}</span>  
            <span class="price"> 基础价格: ${price} 元</span>  
            <button class="estimate-up" data-price="${price}">向上估计</button>  
            <button class="estimate-down" data-price="${price}">向下估计</button>  
            <span class="estimated"></span>  
            <span class="feedback"></span>  
        `;  
        toysContainer.appendChild(toyElement);  
    });  
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
    let totalEstimatedCost = 0;  
    let estimationText = '';  
    let allEstimated = true;
    let allCorrect = true; // 标记所有估算是否正确

    estimates.forEach((estimate, index) => {  
        const value = parseInt(estimate.getAttribute('data-value'));  
        const direction = estimate.getAttribute('data-direction');  
        const feedback = estimate.parentNode.querySelector('.feedback').textContent;

        if (isNaN(value)) {
            allEstimated = false;
        }

        if (feedback !== '正确！') {
            allCorrect = false;
        }

        totalEstimatedCost += isNaN(value) ? 0 : value;
        estimationText += `${isNaN(value) ? '未估算' : `${value} 元`}${index < estimates.length - 1 ? ' + ' : ''}`;  
    });  

    const currentMoney = parseInt(document.getElementById('money').innerText);  
    const resultText = totalEstimatedCost <= currentMoney ? "钱够" : "钱不够";  
    const comparisonText = `${totalEstimatedCost} 元 <= ${currentMoney} 元`;  

    if (!allEstimated) {
        alert("请完成所有玩具的估算！");
        return;
    }

    document.getElementById('estimations').innerText = `${estimationText} = ${totalEstimatedCost} 元，${resultText}，因为 ${comparisonText}。`;  

    // 最终验证所有估算是否符合要求
    if (allCorrect) {
        alert("所有估算均正确！");
    } else {
        alert("存在错误的估算！");
        // 可以进一步高亮显示错误的估算
    }
}
