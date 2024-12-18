document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('startDownload');
    const toggleButton = document.getElementById('toggleAutoSave');
    const statusDiv = document.getElementById('status');
    let autoSaveEnabled = false;

    async function getCurrentTab() {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        return tab;
    }

    async function sendMessageToContentScript(message) {
        try {
            const tab = await getCurrentTab();
            const response = await chrome.tabs.sendMessage(tab.id, message);
            statusDiv.textContent = response?.message || '操作完成';
        } catch (error) {
            statusDiv.textContent = '操作失败: ' + error.message;
            console.error('Error:', error);
        }
    }

    startButton.addEventListener('click', async function() {
        statusDiv.textContent = '正在下载当前页...';
        await sendMessageToContentScript({action: "downloadCurrent"});
    });

    toggleButton.addEventListener('click', async function() {
        autoSaveEnabled = !autoSaveEnabled;
        toggleButton.textContent = `自动保存模式: ${autoSaveEnabled ? '开启' : '关闭'}`;
        statusDiv.textContent = `正在${autoSaveEnabled ? '开启' : '关闭'}自动保存...`;
        await sendMessageToContentScript({
            action: "toggleAutoSave",
            enabled: autoSaveEnabled
        });
    });
});
