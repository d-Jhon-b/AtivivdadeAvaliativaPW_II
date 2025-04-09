// async function excluirUsuario(url, element) {
//     console.log("chegou1")
//     if (confirm("Tem certeza que deseja excluir este usuário?")) {
//         try {
//             const response = await fetch(url, {
//                 method: 'DELETE',
//             });
//             console.log("chegou2")
//             if (response.ok) {
//                 // Remover a linha do usuário da tabela/lista
//                 element.parentNode.remove();
//                 alert("Usuário excluído com sucesso!");
//             } else {
//                 const errorData = await response.json();
//                 alert(`Erro ao excluir usuário: ${errorData.message || 'Erro desconhecido'}`);
//             }
//         } catch (error) {
//             console.error("Erro ao fazer a requisição DELETE:", error);
//             alert("Ocorreu um erro ao tentar excluir o usuário.");
//         }
//     }
// }

