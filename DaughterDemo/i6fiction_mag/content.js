// 设置全局变量以跟踪状态
window.magazineDownloader = window.magazineDownloader || {
    pageCount: 0,
    MAX_PAGES: 3,  // 修改为 8，允许下载 8 页
    autoSaveEnabled: false,
    downloadedImages: new Set()  // 用于存储已下载图片的URL
};

// 监听来自popup的消息
chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "downloadCurrent") {
        downloadImagesOnPage();
        sendResponse({ message: "开始下载当前页面" });
    } else if (request.action === "toggleAutoSave") {
        window.magazineDownloader.autoSaveEnabled = request.enabled;
        window.magazineDownloader.pageCount = 0;
        if (window.magazineDownloader.autoSaveEnabled) {
            handlePage();
        }
        sendResponse({ message: `自动保存模式已${window.magazineDownloader.autoSaveEnabled ? '开启' : '关闭'}` });
    }
    return true;
});

// 处理页面下载和翻页
function handlePage() {
    if (window.magazineDownloader.pageCount >= window.magazineDownloader.MAX_PAGES) {
        console.log('已达到最大页数限制');
        window.magazineDownloader.autoSaveEnabled = false;
        return;
    }

    window.magazineDownloader.pageCount++;
    console.log(`开始处理第 ${window.magazineDownloader.pageCount} 页`);

    if (clickNextPage()) {
        console.log('翻页成功，等待页面加载...');
        // 等待页面加载完成后再进行下一步
        setTimeout(() => {
            downloadImagesOnPage(); // 下载当前页图片
            handlePage(); // 继续处理下一页
        }, 3000); // 延时等待页面加载，视情况调整
    } else {
        console.log('未找到翻页按钮，自动保存已停止。');
        window.magazineDownloader.autoSaveEnabled = false;
    }
}

// 点击下一页按钮
function clickNextPage() {
    const nextButton = document.querySelector('li.nextPage');
    if (nextButton) {
        nextButton.click();
        return true;
    }
    return false;
}

// 监听URL的hash变化来下载图片
window.addEventListener('hashchange', function() {
    console.log('检测到URL变化，正在检查新页面的图片...');
    downloadImagesOnPage();  // 每次URL变化时重新下载
}, false);

// 下载页面上的图片
function downloadImagesOnPage() {
    setTimeout(() => { // 增加延时确保页面加载完成
        const images = document.querySelectorAll('img.slide-img');
        images.forEach((img, index) => {
            const src = img.getAttribute('src');
            // 只下载有意义的图片，过滤掉无关的图片，例如loading图
            if (src && src.includes('big.mg;vpn_img') && !src.includes('/assets/img/loadingBg.png') && !window.magazineDownloader.downloadedImages.has(src)) {
                console.log(`找到有效图片 ${index + 1}: ${src}`);
                const filename = `page${window.magazineDownloader.pageCount}_${index + 1}.webp`; // 确保文件名带 .webp 后缀
                downloadImage(src, filename);
                window.magazineDownloader.downloadedImages.add(src);  // 添加图片URL到已下载集合
            }
        });
    }, 1000); // 根据页面加载速度调整这个延时
}

// 下载图片
function downloadImage(src, filename) {
    console.log(`开始下载图片: ${src} 保存为: ${filename}`);
    chrome.runtime.sendMessage({action: "download", url: src, filename: filename});
}

// 初次加载页面时也需要查找图片
document.addEventListener('DOMContentLoaded', () => {
    if (window.magazineDownloader.autoSaveEnabled) {
        downloadImagesOnPage(); // 页面初始化时检查一次图片
    }
});
