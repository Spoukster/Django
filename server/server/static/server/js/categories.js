const renderCategory = ({id, name}) => (
    `
        <li class="categories__item">
            <span class="categories__item-name">
                ${ name }
            </span>
            <a href="/categories/${ id }" class="categories__item-link">
                Ссылка на ${ name }
            </a>
        </li>
    `
)