/* Isi untuk file js/toast.js */

(function () {
    const toastComponent = document.getElementById('toast-component');
    const toastIcon = document.getElementById('toast-icon');
    const toastTitle = document.getElementById('toast-title');

    // Konfigurasi kelas dan ikon berdasarkan tipe
    const typeClasses = {
        'success': {
            icon: '✔',
            iconClasses: 'text-green-600',
            title: 'Success',
        },
        'error': {
            icon: '✖',
            iconClasses: 'text-red-600',
            title: 'Error',
        },
        'info': {
            icon: 'i',
            iconClasses: 'text-blue-600',
            title: 'Info',
        }
    };

    let toastTimeout = null;

    // Utility untuk menghapus semua kelas warna dinamis dari ikon
    function clearIconClasses(element) {
        const classesToRemove = [
            'text-green-600', 'text-red-600', 'text-blue-600'
        ];
        element.classList.remove(...classesToRemove);
    }

    /**
     * Menampilkan notifikasi toast.
     */
    window.showToast = function (title, message, type = 'info', duration = 4000) {

        // 1. Reset/Clear previous state
        if (toastTimeout) {
            clearTimeout(toastTimeout);
        }
        clearIconClasses(toastIcon);

        // 2. Determine configuration
        const config = typeClasses[type] || typeClasses['info'];

        // 3. Set content
        toastTitle.textContent = title || config.title;
        document.getElementById('toast-message').textContent = message;

        // 4. Set dynamic styles (Hanya Icon)
        toastIcon.textContent = config.icon;
        toastIcon.classList.add(...config.iconClasses.split(' '));

        // 5. Show toast (Tarik toast ke atas)
        toastComponent.classList.remove('translate-y-64', 'opacity-0');
        toastComponent.classList.add('opacity-100');

        // 6. Set timeout to hide (Dorong toast ke bawah setelah durasi)
        toastTimeout = setTimeout(() => {
            toastComponent.classList.remove('opacity-100');
            toastComponent.classList.add('translate-y-64', 'opacity-0');
        }, duration);
    };
})();