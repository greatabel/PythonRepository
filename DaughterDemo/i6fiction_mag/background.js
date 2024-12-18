chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "download") {
        console.log('开始下载:', request.filename);
        chrome.downloads.download({
            url: request.url,
            filename: `magazine_downloads/${request.filename}`,
            saveAs: false,
            conflictAction: 'uniquify'
        }, (downloadId) => {
            if (chrome.runtime.lastError) {
                console.error('下载错误:', chrome.runtime.lastError);
            } else {
                console.log('下载成功:', request.filename);
            }
        });
    }
    return true;
});
