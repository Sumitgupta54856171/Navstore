import React from 'react';
import ItemCard from './ItemCard';

const sampleItems = [
  {
    id: 1,
    imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDykslgE83yWvgu2tU69olaeqOVIFdwPeLyg&s',
    name: 'Classic T-Shirt',
    description: 'A comfortable and stylish t-shirt made from 100% premium cotton.',
    price: '24.99',
  },
  {
    id: 2,
    imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDykslgE83yWvgu2tU69olaeqOVIFdwPeLyg&s',
    name: 'Denim Jeans',
    description: 'Perfectly fitted denim jeans for a modern and timeless look.',
    price: '89.99',
  },
  {
    id: 3,
    imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDykslgE83yWvgu2tU69olaeqOVIFdwPeLyg&s',
    name: 'Leather Jacket',
    description: 'A sleek and durable leather jacket to elevate your style.',
    price: '199.99',
  },
    {
    id: 4,
    imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDykslgE83yWvgu2tU69olaeqOVIFdwPeLyg&s',
    name: 'Sneakers',
    description: 'Lightweight and comfortable sneakers for everyday wear.',
    price: '120.00',
  },
];

function Itemlist() {
  return (
    <div className="container mx-auto px-4 py-8">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
        {sampleItems.map(item => (
          <ItemCard key={item.id} item={item} />
        ))}
      </div>
    </div>
  );
}
export default Itemlist;