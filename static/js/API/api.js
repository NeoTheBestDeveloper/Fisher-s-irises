const predictIrisSortAPI = async (irisProps) => {
	// Send iris props to server.
	let response = await fetch("/predict", {
		method: "POST",
		body: JSON.stringify({
			payload: irisProps,
		}),
	});

	if (response.ok) {
		let predict_sort = await response.json();
		return predict_sort;
	} else {
		showAlert("Ошибка" + response.status, "error");
	}
};
