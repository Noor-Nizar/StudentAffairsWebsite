function confirmAction() {
    var confirmAction = confirm("Are you sure to execute this action?");
    if (confirmAction) {
        alert("Action successfully executed");
        return true;
    } else {
        alert("Action canceled");
        return false;
    }
}

function validate() {
    var firstname = document.getElementsByName("firstname")[0].value;
    var lastname = document.getElementsByName("lastname")[0].value;
    var email = document.getElementsByName("email").value;
    var phone = document.getElementById("phone").value;
    var id = document.getElementsByName("ID")[0].value;
    var Gender = document.getElementsByName("gender");
    var date = document.getElementsByName("date of birth");
    var level = document.getElementById("Level").value;
    var gpa = document.getElementById("GPA").value;
    var status = document.getElementsByName("Status");


    //write input validation for above varaibles
    if (firstname == "" || lastname == "" || email == "" || phone == "" || date[0].value == "" || id == "") {
        window.alert("Please fill all the fields");
        return false;
    } else if (phone.length != 11) {
        window.alert("Please enter a valid phone number");
        return false;
    } else if (gpa > 4 || gpa < 0) {
        window.alert("Invalid Input Please Enter GPA between 0 and 4");
        return false;
    } else if (level < 0 || level > 4) {
        window.alert("Invalid Input Please Enter Level between 0 and 4");
        return false;
    } else if (!status[0].checked && !status[1].checked) {
        window.alert("Please Select Status");
        return false;
    } else if (!Gender[0].checked && !Gender[1].checked) {
        window.alert("Please Select Gender");
        return false;
    } else {
        confirmAction();
    }

}

function dep_pop() {
    var b = document.getElementById("pet-select").value;
    var a = document.getElementById("lvl1").value;
    if (a == 3 && b != "General" && b != "") {
        window.alert(" Department successfully assigned");
    } else {
        window.alert("Invalid Info to perform Department assignment")
    }
};

function confDelete() {
    var r = confirm("Are you sure you want to delete this student?");
    if (r == true) {
        window.location.href = "RemoveStudent.py";
        return true;
    }
    else
        return false;
}

function confirmEdit() {
    var confirmAction = confirm("Are you sure to execute this action?");
    if (confirmAction) {
        alert("Action successfully executed");
        return true;
    } else {
        alert("Action canceled");
        return false;
    }
}

function validate() {
    var firstname = document.getElementsByName("firstname")[1].value;
    var lastname = document.getElementsByName("lastname")[1].value;
    var email = document.getElementsByName("email")[1].value;
    var phone = document.getElementsByName("phone")[1].value;
    var id = document.getElementsByName("ID")[0].value;
    var Gender = document.getElementsByName("gender");
    var date = document.getElementsByName("date of birth");
    var level = document.getElementsByName("Level")[1].value;
    var gpa = document.getElementsByName("GPA")[1].value;
    var status = document.getElementsByName("Status");


    //write input validation for above varaibles
    if (firstname == "" || lastname == "" || email == "" || date[1].value == "" || id == "") {
        window.alert("Please fill all the fields");
        return false;
    } else if (phone.length != 11 || phone == "") {
        window.alert("Please enter a valid phone number");
        return false;
    } else if (gpa > 4 || gpa < 0 || gpa == "") {
        window.alert("Invalid Input Please Enter GPA between 0 and 4");
        return false;
    } else if (level < 0 || level > 4 || level == "") {
        window.alert("Invalid Input Please Enter Level between 0 and 4");
        return false;
    } else if (!status[2].checked && !status[3].checked) {
        window.alert("Please Select Status");
        return false;
    } else if (!Gender[2].checked && !Gender[3].checked) {
        window.alert("Please Select Gender");
        return false;
    } else {
        return confirmEdit();
    }

}

function myFunc() {
    window.location.href = "ViewAllStudents.html";
}

function lol() {
    var xhttp = new XMLHttpRequest();
    sid = document.getElementById("sid").value;
    n = "getStudent/" + sid;
    console.log(sid);
    xhttp.open("GET", n, false);
    xhttp.send();
    values = xhttp.response;
    console.log(values);
    document.getElementById("result").innerHTML = values;
    return 0;
}