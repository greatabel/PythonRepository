document.addEventListener('DOMContentLoaded', function() {  
    setupGame();  
    document.getElementById('calculate-button').addEventListener('click', calculate);  
});  
  
function setupGame() {  
    const basePrices = [101, 112, 123, 134, 145, 119]; // 确保所有的价格都需要估算  
    const toys = [  
        { name: "玩具熊", basePrice: basePrices[Math.floor(Math.random() * basePrices.length)] },  
        { name: "玩具车", basePrice: basePrices[Math.floor(Math.random() * basePrices.length)] }  
    ];  
  
    const toysContainer = document.getElementById('toys');  
    toysContainer.innerHTML = '';  
  
    const money = Math.floor(Math.random() * 301) + 100; // 随机生成100到400之间的金额  
    document.getElementById('money').textContent = money;  
  
    toys.forEach(toy => {  
        const price = toy.basePrice;  
        const toyElement = document.createElement('div');  
        toyElement.className = 'toy';  
        toyElement.innerHTML = `  
            <span class="name">${toy.name}</span>  
            <span class="price">${price} 元</span>  
            <button onclick="estimate(this, ${price}, 'up', ${money})">向上估计</button>  
            <button onclick="estimate(this, ${price}, 'down', ${money})">向下估计</button>  
            <span class="estimated"></span>  
            <span class="feedback"></span>  
        `;  
        toysContainer.appendChild(toyElement);  
    });  
}  
  
function estimate(buttonElement, price, direction, money) {  
    const estimatedElement = buttonElement.parentNode.querySelector('.estimated');  
    const feedbackElement = buttonElement.parentNode.querySelector('.feedback');  
    const roundedPrice = direction === 'up' ? Math.ceil(price / 10) * 10 : Math.floor(price / 10) * 10;  
    estimatedElement.textContent = `估计值：${roundedPrice} 元`;  
    estimatedElement.setAttribute('data-value', roundedPrice);  
  
    // 更新逻辑：钱包金额不足时，向下估计为正确；钱包金额足够时，向上估计为正确  
    const isMoneySufficient = money >= price;  
    const canStillBuy = money >= roundedPrice; // 确保估计后的价格仍然可以购买商品  
    const isEstimationCorrect = (isMoneySufficient && direction === 'up') || (!isMoneySufficient && direction === 'down') || canStillBuy;  
  
    if (isEstimationCorrect) {  
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
  
    estimates.forEach((estimate, index) => {  
        const value = parseInt(estimate.getAttribute('data-value'));  
        totalEstimatedCost += value;  
        estimationText += `${value} 元${index < estimates.length - 1 ? ' + ' : ''}`;  
    });  
  
    const currentMoney = parseInt(document.getElementById('money').innerText);  
    const resultText = totalEstimatedCost <= currentMoney ? "钱够" : "钱不够";  
    const comparisonText = `${totalEstimatedCost} 元 <= ${currentMoney} 元`;  
  
    document.getElementById('estimations').innerText = `${estimationText} = ${totalEstimatedCost} 元，${resultText}，因为 ${comparisonText}。`;  
  
    // 如果钱不够，验证所有的估计是否都向下  
    if (totalEstimatedCost > currentMoney) {  
        const feedbackElements = document.querySelectorAll('.feedback');  
        feedbackElements.forEach(feedback => {  
            feedback.textContent = '正确！';  
            feedback.style.color = 'green';  
        });  
    }  
}  

