function getcle(get_cle) {
  // 1. تحويل النص المدخل إلى رقم صحيح كبير لضمان الدقة
  let inputVal = BigInt(get_cle.toString().replace(/\s/g, "")); // إزالة الفراغات إن وجدت

  // 2. تطبيق الخوارزمية
  let ccp = inputVal * 100n;
  let n1 = Number(ccp % 97n);
  let n2 = 85;

  if (n1 + 85 > 97) {
    n2 = n1 + 85 - 97;
  } else {
    n2 = n1 + 85;
  }

  let cle = n2 == 97 ? 97 : 97 - n2;

  // 3. إرجاع النتيجة مع التأكد من أنها رقمين (مثلاً 05 بدل 5)
  return cle.toString().padStart(2, "0");
}

// ربط الحقول
let ccpInput = document.getElementById("ccp");
let cleInput = document.getElementById("cle");

ccpInput.onkeyup = function () {
  let val = ccpInput.value;
  if (val === "" || isNaN(val)) {
    cleInput.value = ""; // مسح النتيجة إذا كان الحقل فارغاً
    return;
  }
  cleInput.value = getcle(val);
};

// حساب التقسيط

let totalAmount = document.getElementById("totalAmount");
let annualRate = document.getElementById("annualRate");
let totalAmounttwo = document.getElementById("totalAmounttwo");
let annualRatetwo = document.getElementById("annualRatetwo");
let months = document.getElementById("months");
let fprice = document.getElementById("fprice");
let monthc = document.getElementById("monthc");
let perpri = document.getElementById("perpri");
let monthlycut = document.getElementById("monthlycut");
let discountprice = document.getElementById("discountprice");
// دالة لتقييد عدد الخانات
function limitLength(element, max) {
    element.oninput = function() {
        if (this.value.length > max) {
            this.value = this.value.slice(0, max);
        }
        update(); // تحديث الحسابات فوراً بعد التعديل
    };
}

// تطبيق القيود:
limitLength(months, 2);        // الشهور: خانتين فقط (مثلاً 24 شهر)
limitLength(annualRate, 2);    // النسبة الأولى: خانتين فقط (مثلاً 15%)
limitLength(annualRatetwo, 2); // النسبة الثانية: خانتين فقط (مثلاً 10%)

// 1. تصحيح دالة الحساب (أصبحت تعيد القيمة مباشرة)
function calculateInstallment(totalWithPercentage, months) {
  if (months === 0) return 0;
  let monthly = totalWithPercentage / months;
  return monthly.toFixed(2); // تعيد نصاً منسقاً
}

function update() {
  try {
    // حساب المبالغ باستخدام eval لدعم العمليات الحسابية
    let totalVal1 = eval(totalAmount.value) || 0;
    let totalVal2 = eval(totalAmounttwo.value) || 0;

    // عرض مجموع السلعتين قبل الفوائد
    let globalRawTotal = totalVal1 + totalVal2;
    fprice.innerHTML = globalRawTotal;

    // جلب نسب الفائدة والشهور
    let ann1 = parseFloat(annualRate.value) || 0;
    let ann2 = parseFloat(annualRatetwo.value) || 0;
    let mon = parseInt(months.value) || 0;
    let discount = parseFloat(discountprice.value) || 0;

    // حساب الفوائد لكل سلعة على حدة
    let totalWithPer1 = totalVal1 * (1 + ann1 / 100);
    let totalWithPer2 = totalVal2 * (1 + ann2 / 100);

    // المجموع النهائي المطلوب سداده
    let globalTotalWithPer = totalWithPer1 + totalWithPer2 - discount;
    perpri.innerHTML = globalTotalWithPer.toFixed(2);

    // تحديث نص النسبة المئوية المعروض
    perce.innerHTML = totalVal2 > 0 ? `${ann1}% + ${ann2}%` : `${ann1}%`;
    monthc.innerHTML = mon;

    // 2. تصحيح طريقة استدعاء النتيجة
    if (globalTotalWithPer > 0 && mon > 0) {
      let result = calculateInstallment(globalTotalWithPer, mon);
      monthlycut.innerHTML = result; // هنا النتيجة مباشرة وليست result.monthlyPayment
    } else {
      monthlycut.innerHTML = "0.00";
    }
  } catch (e) {
    console.log("جاري إكمال العملية الحسابية...");
  }
}

// 3. ربط الأحداث لضمان التحديث التلقائي
totalAmount.onkeyup = update;
annualRate.onkeyup = update;
totalAmounttwo.onkeyup = update;
annualRatetwo.onkeyup = update;
months.onkeyup = update;
discountprice.onkeyup = update;

let butonsec = document.getElementById("iconplus");
let iconminus = document.getElementById("iconminus");
let iconplusdis = document.getElementById("iconplusdis");
let iconminusdis = document.getElementById("iconminusdis");
let secondmonton = document.getElementById("secondmonton");
let disbut = document.getElementById("disbut");
butonsec.onclick = function () {
  secondmonton.classList.remove("hide");
  this.classList.add("hide");
};
iconminus.onclick = function () {
  secondmonton.classList.add("hide");
  butonsec.classList.remove("hide");
  totalAmounttwo.value = "";
  annualRatetwo.value = "";
  update()
};
iconplusdis.onclick = function () {
  disbut.classList.remove("hide");
  iconplusdis.classList.add("hide");
};
iconminusdis.onclick = function () {
  disbut.classList.add("hide");
  iconplusdis.classList.remove("hide");
  discountprice.value = "";
  update();
};
