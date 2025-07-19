import React from 'react';

function ItemCard({ item }) {
  const { id, imageUrl, name, description, price } = item;

  return (
    <div className="bg-white rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300 overflow-hidden">
      <div className="relative pb-48 overflow-hidden">
        <img src={imageUrl} alt={name} className="absolute inset-0 h-full w-full object-cover" />
      </div>
      <div className="p-4">
        <h3 className="text-lg font-semibold mb-2 text-black">{name}</h3>
        <p className="text-gray-600 text-sm mb-4 h-20">{description}</p>
        <div className="flex items-center justify-between mb-4">
          <span className="text-xl font-bold text-gray-800">${price}</span>
          <button className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600 transition-colors">
            Add to Cart
          </button>
        </div>
        <a href={`/items/${id}`} className="block text-center bg-gray-200 text-gray-700 py-2 px-4 rounded hover:bg-gray-300 transition-colors">
            View Details
        </a>
      </div>
    </div>
  );
}

export default ItemCard;
