import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import data from "./data";
import "./RecipeDetail.css";

const RecipeDetail = () => {
  const { id } = useParams();
  console.log("Рецепт ID:", id); // Для отладки
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    console.log("Received ID:", id);
    // Находим рецепт по id
    const foundRecipe = data.recipes.find((recipe) => recipe.id === id);
    if (foundRecipe) {
      setRecipe(foundRecipe);
    } else {
      console.error("Рецепт не найден");
    }
  }, [id]);

  if (!recipe) return <p>Загрузка...</p>; // Показываем сообщение, пока данные загружаются

  return (
    <div className="recipe-detail">
      <h2>{recipe.title}</h2>
      <h3>Ингредиенты:</h3>
      <ul>
        {recipe.ingredients.map((ingredient, index) => (
          <li key={index}>{ingredient}</li>
        ))}
      </ul>
      <h3 className="instructions">Рецепт:</h3>
      <p>{recipe.instructions}</p>
    </div>
  );
};

export default RecipeDetail;
