document.addEventListener("DOMContentLoaded", function () {
    var alerts = document.querySelectorAll(".alert");
    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = "opacity 0.5s";
            alert.style.opacity = "0";
            setTimeout(function () {
                alert.remove();
            }, 500);
        }, 5000);
    });

    var deleteLinks = document.querySelectorAll(".delete-confirm");
    deleteLinks.forEach(function (link) {
        link.addEventListener("click", function (e) {
            if (!confirm("确定要删除吗？此操作不可撤销。")) {
                e.preventDefault();
            }
        });
    });

    var tables = document.querySelectorAll(".data-table");
    tables.forEach(function (table) {
        var rows = table.querySelectorAll("tbody tr");
        rows.forEach(function (row) {
            row.addEventListener("mouseenter", function () {
                this.style.background = "#fdf6ee";
            });
            row.addEventListener("mouseleave", function () {
                this.style.background = "";
            });
        });
    });
});
