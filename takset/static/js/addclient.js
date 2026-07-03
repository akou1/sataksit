const TaksitSystem = {
  // 1. تعريف كافة العناصر (Selectors)
  elements: {
    ccp: document.getElementById("ccp"),
    cle: document.getElementById("cle"),
    // total1: document.getElementById("totalAmount"),
    // rate1: document.getElementById("annualRate"),
    // total2: document.getElementById("totalAmounttwo"),
    // rate2: document.getElementById("annualRatetwo"),
    // months: document.getElementById("months"),
    // discount: document.getElementById("discountprice"),
    // عناصر العرض (Display)
    // fprice: document.getElementById("fprice"),
    // perce: document.getElementById("perce"),
    // monthc: document.getElementById("monthc"),
    // perpri: document.getElementById("perpri"),
    // monthlycut: document.getElementById("monthlycut"),
    // // أزرار التحكم
    // plusIcon: document.getElementById("iconplus"),
    // minusIcon: document.getElementById("iconminus"),
    // plusDis: document.getElementById("iconplusdis"),
    // minusDis: document.getElementById("iconminusdis"),
    // secondSection: document.getElementById("secondmonton"),
    // disContainer: document.getElementById("disbut"),
    btnPrint: document.getElementById("bobo"),
    // datecute: document.getElementById("datecute"),
  },

  // 2. محرك حساب المفتاح (CCP Key)
  getCleCCP: function (val) {
    if (val === "" || isNaN(val)) return "";
    let inputVal = BigInt(val.toString().replace(/\s/g, ""));
    let ccp = inputVal * 100n;
    let n1 = Number(ccp % 97n);
    let n2 = n1 + 85 > 97 ? n1 + 85 - 97 : n1 + 85;
    let cle = n2 == 97 ? 97 : 97 - n2;
    return cle.toString().padStart(2, "0");
  },

  // 3. المحرك الرياضي للتقسيط
  updateUI: function () {
    try {
      const el = this.elements;
      let v1 = eval(el.total1.value) || 0;
      let v2 = eval(el.total2.value) || 0;
      let ann1 = parseFloat(el.rate1.value) || 0;
      let ann2 = parseFloat(el.rate2.value) || 0;
      let mon = parseInt(el.months.value) || 0;
      let disc = parseFloat(el.discount.value) || 0;

      // الحسابات
      let totalWithPer1 = v1 * (1 + ann1 / 100);
      let totalWithPer2 = v2 * (1 + ann2 / 100);
      let globalTotal = totalWithPer1 + totalWithPer2 - disc;

      // تحديث الواجهة
      el.fprice.innerHTML = (v1 + v2).toFixed(2);
      el.perpri.innerHTML = globalTotal.toFixed(2);
      el.monthc.innerHTML = mon;
      el.perce.innerHTML = v2 > 0 ? `${ann1}% + ${ann2}%` : `${ann1}%`;

      if (globalTotal > 0 && mon > 0) {
        el.monthlycut.innerHTML = (globalTotal / mon).toFixed(2);
      } else {
        el.monthlycut.innerHTML = "0.00";
      }
    } catch (e) {
      console.log("Waiting for valid math...");
    }
  },
  Payload: function () {
    const el = this.elements;

    // 1. تجميع كل البيانات في كائن واحد (طرد بريدي)
    return {
      personal_info_sy: {
        ccp: el.ccp.value,
        cle: el.cle.value,
        first_name: document.getElementById("firstName").value,
        last_name: document.getElementById("lastName").value,
        // birth_date: document.getElementById("birthDate").value,
        // birth_place: document.getElementById("birthPlace").value,
        // address: document.getElementById("address").value,
        // national_id: document.getElementById("nationalID").value,
        // id_issue_date: document.getElementById("idIssueDate").value,
        // phone: document.getElementById("phone").value,
        // datecute: el.datecute.value,
      },
      // financial_info: {
      //   amount_1: el.total1.value,
      //   rate_1: el.rate1.value,
      //   amount_2: el.total2.value,
      //   rate_2: el.rate2.value,
      //   months: el.months.value,
      //   discount: el.discount.value,
      //   total_raw: el.fprice.innerText,
      //   final_total: el.perpri.innerText,
      //   monthly_cut: el.monthlycut.innerText,
      // },
    };
  },

  // 4. دالة التشغيل والربط (Initialization)
  init: function () {
    const self = this;
    const el = this.elements;

    // ربط الـ CCP
    // el.ccp.onkeyup = () => (el.cle.value = self.getCleCCP(el.ccp.value));

    // // ربط حقول الحسابات
    // const inputs = [
    //   el.total1,
    //   el.rate1,
    //   el.total2,
    //   el.rate2,
    //   el.months,
    //   el.discount,
    // ];
    // inputs.forEach((input) => {
    //   if (input) input.onkeyup = () => self.updateUI();
    // });

    // // قيود الطول (Length Limits)
    // this.setLimit(el.months, 2);
    // this.setLimit(el.rate1, 2);
    // this.setLimit(el.rate2, 2);

    // // أزرار الإظهار والإخفاء
    // el.plusIcon.onclick = () => {
    //   el.secondSection.classList.remove("hide");
    //   el.plusIcon.classList.add("hide");
    // };
    // el.minusIcon.onclick = () => {
    //   el.secondSection.classList.add("hide");
    //   el.plusIcon.classList.remove("hide");
    //   el.total2.value = "";
    //   el.rate2.value = "";
    //   self.updateUI();
    // };
    // el.plusDis.onclick = () => {
    //   el.disContainer.classList.remove("hide");
    //   el.plusDis.classList.add("hide");
    // };
    // el.minusDis.onclick = () => {
    //   el.disContainer.classList.add("hide");
    //   el.plusDis.classList.remove("hide");
    //   el.discount.value = "";
    //   self.updateUI();
    // };
    if (el.btnPrint) {
      el.btnPrint.onclick = (e) => {
        e.preventDefault();

        const data = self.Payload(); // جلب البيانات المحدثة
        const csrf = document.querySelector("[name=csrfmiddlewaretoken]").value;

        console.log("إرسال البيانات:", data);

        fetch("/addnew/addclient.html/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf,
          },
          body: JSON.stringify(data),
        })
          .then((res) => res.json())
          .then(
            (resData) => {
              alert("رد السيرفر: " + resData.msg);
              if (resData.status === "success") {
              window.location.reload(); // إعادة إنعاش الصفحة لمشاهدة التعديل الجديد
            }
          })
          .catch((err) => console.error("Error:", err));
      };
    }
  },

  setLimit: function (element, max) {
    element.oninput = () => {
      if (element.value.length > max)
        element.value = element.value.slice(0, max);
      this.updateUI();
    };
  },

  // أضف هذه الدوال داخل كائن TaksitSystem في ملف main.js
  // أضف هذه الدالة داخل كائن TaksitSystem قبل القوس النهائي
};

// تشغيل النظام بالكامل
TaksitSystem.init();



