const showAlert = (alert, type) => {
	const form_alert = document.querySelector("#form-alert");
	form_alert.innerText = alert;
	form_alert.className = type;
};

const validateIrisProps = (irisProps) => {
	// Check user data on data type (we need number).
	irisProps = irisProps.map((x) => x.isdigit);
	if (irisProps.includes(false)) {
		showAlert("Неверные данные", "error");
		return false;
	} else {
		return true;
	}
};

const predictIrisSort = async (f) => {
	// Prepare and send iris props to API level.
	let irisProps = [f[0].value, f[1].value, f[2].value, f[3].value];
	if (validateIrisProps(irisProps)) {
		irisProps = irisProps.map(parseFloat);
		let predict_sort = await predictIrisSortAPI(irisProps);
		showAlert(predict_sort.payload, "message");
	}
};
