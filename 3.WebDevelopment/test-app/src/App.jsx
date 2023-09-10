function App() {
  return (
    <div className="flex justify-center items-center w-screen h-screen bg-slate-100">
      <div className="bg-white rounded-xl shadow-md w-[40%] h-[66%] flex flex-col justify-between">
        <img
          className="w-full h-[40%] rounded-xl"
          src="https://via.placeholder.com/300"
          alt="Sample Image"
        />
        <div className="p-6 w-full h-full flex flex-col justify-between">
          <h2 className="text-md font-bold text-black">Bitcoin (BTC)</h2>
          <p className="text-gray-500">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          </p>
          <p className="text-gray-500">Order Type: MARKET</p>
          <div className="text-gray-500">
            <span>Price: </span>
            <span className="text-blue-500 text-xl font-extrabold">
              990,000 THB
            </span>
          </div>
          <button className="w-full bg-blue-500 rounded-xl max-w-fit">
            Place Order
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
