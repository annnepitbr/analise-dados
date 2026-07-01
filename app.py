"""
Bip de Senha - Fast Food (Ex: Giraffas)
----------------------------------------
Simulação de uma torre de bips utilizados como senha de pedidos em uma
lanchonete fast food, implementada com a estrutura de dados PILHA (Stack),
seguindo o princípio LIFO (Last In, First Out).

Funcionalidades:
- Adicionar bip  -> empilha (push) um novo bip no topo da torre
- Retirar bip    -> desempilha (pop) o bip do topo e entrega ao cliente
- Mostrar bip atual -> consulta (peek) o bip que está no topo da torre,
                       sem removê-lo
"""

from dataclasses import dataclass, field
from datetime import datetime

import streamlit as st


# ---------------------------------------------------------------------------
# ESTRUTURA DE DADOS: PILHA (STACK) - LIFO
# ---------------------------------------------------------------------------
class PilhaDeBips:
    """
    Implementação de uma Pilha (Stack) para representar a torre física
    de bips do restaurante.

    O último bip colocado na torre (empilhado) é sempre o primeiro
    a ser retirado (LIFO - Last In, First Out), exatamente como
    acontece com uma torre real de bips empilhados uns sobre os outros.
    """

    def __init__(self):
        self._pilha: list[int] = []

    def empilhar(self, bip: int) -> None:
        """Adiciona (push) um bip no topo da torre."""
        self._pilha.append(bip)

    def desempilhar(self) -> int | None:
        """Remove (pop) e retorna o bip do topo da torre."""
        if self.esta_vazia():
            return None
        return self._pilha.pop()

    def topo(self) -> int | None:
        """Consulta (peek) o bip que está no topo, sem remover."""
        if self.esta_vazia():
            return None
        return self._pilha[-1]

    def esta_vazia(self) -> bool:
        return len(self._pilha) == 0

    def tamanho(self) -> int:
        return len(self._pilha)

    def como_lista(self) -> list[int]:
        """Retorna a pilha do topo para a base (ordem de retirada)."""
        return list(reversed(self._pilha))


@dataclass
class Entrega:
    pedido: int
    bip: int
    horario: str


# ---------------------------------------------------------------------------
# ESTADO DA SESSÃO (persistência entre interações do Streamlit)
# ---------------------------------------------------------------------------
def inicializar_estado(qtd_inicial: int = 10) -> None:
    if "pilha" not in st.session_state:
        pilha = PilhaDeBips()
        for numero in range(1, qtd_inicial + 1):
            pilha.empilhar(numero)
        st.session_state.pilha = pilha
        st.session_state.proximo_bip = qtd_inicial + 1
        st.session_state.proximo_pedido = 1
        st.session_state.historico: list[Entrega] = []
        st.session_state.bip_atual_cliente = None  # último bip entregue


def resetar_estado(qtd_inicial: int) -> None:
    for chave in ["pilha", "proximo_bip", "proximo_pedido", "historico", "bip_atual_cliente"]:
        st.session_state.pop(chave, None)
    inicializar_estado(qtd_inicial)


# ---------------------------------------------------------------------------
# INTERFACE STREAMLIT
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Bip de Senha - Fast Food", page_icon="🔔", layout="wide")

st.title("🔔 Bip de Senha - Fast Food")
st.caption(
    "Simulação da torre de bips utilizada em redes como o **Giraffas** para "
    "controlar a entrega de pedidos, implementada com a estrutura de dados "
    "**Pilha (Stack / LIFO)**."
)

with st.sidebar:
    st.header("⚙️ Configurações")
    qtd_inicial = st.number_input(
        "Quantidade inicial de bips na torre", min_value=1, max_value=100, value=10
    )
    if st.button("🔄 Reiniciar torre de bips", use_container_width=True):
        resetar_estado(qtd_inicial)
        st.rerun()

    st.divider()
    st.markdown(
        """
        **Como funciona a pilha (LIFO):**
        - Os bips ficam empilhados um sobre o outro.
        - Ao finalizar um pedido, o caixa retira o bip do **topo**
          da torre e entrega ao cliente.
        - Bips que retornam (clientes que terminaram a refeição)
          voltam para o **topo** da torre.
        - O último bip a entrar é sempre o primeiro a sair.
        """
    )

inicializar_estado(qtd_inicial)
pilha: PilhaDeBips = st.session_state.pilha

# --------------------------- Métricas rápidas ------------------------------
col_m1, col_m2, col_m3 = st.columns(3)
col_m1.metric("📦 Bips disponíveis na torre", pilha.tamanho())
col_m2.metric("🎫 Bip atual (topo da torre)", pilha.topo() if not pilha.esta_vazia() else "—")
col_m3.metric("✅ Pedidos atendidos", len(st.session_state.historico))

st.divider()

col_acoes, col_torre = st.columns([1, 1])

# --------------------------- Ações (funcionalidades) ------------------------
with col_acoes:
    st.subheader("Ações do caixa")

    # Funcionalidade: Mostrar bip atual (peek)
    st.markdown("**👁️ Mostrar bip atual (topo da torre)**")
    if pilha.esta_vazia():
        st.warning("A torre está vazia. Não há bips disponíveis.")
    else:
        st.info(f"O próximo bip a ser entregue é o **Bip #{pilha.topo()}**.")

    st.markdown("---")

    # Funcionalidade: Retirar bip (pop) -> vincula ao pedido e entrega ao cliente
    st.markdown("**➖ Retirar bip (finalizar pedido / entregar ao cliente)**")
    if st.button("Finalizar atendimento e entregar bip", type="primary", use_container_width=True):
        bip_retirado = pilha.desempilhar()
        if bip_retirado is None:
            st.error("Não há bips na torre para entregar!")
        else:
            pedido_atual = st.session_state.proximo_pedido
            st.session_state.proximo_pedido += 1
            st.session_state.bip_atual_cliente = bip_retirado
            st.session_state.historico.insert(
                0,
                Entrega(
                    pedido=pedido_atual,
                    bip=bip_retirado,
                    horario=datetime.now().strftime("%H:%M:%S"),
                ),
            )
            st.success(f"Pedido #{pedido_atual} vinculado ao **Bip #{bip_retirado}** e entregue ao cliente!")

    st.markdown("---")

    # Funcionalidade: Adicionar bip (push) -> repor bip na torre
    st.markdown("**➕ Adicionar bip (repor bip na torre)**")
    modo_add = st.radio(
        "Como deseja adicionar o bip?",
        ["Repor bip devolvido (topo)", "Cadastrar bip novo (sequencial)"],
        horizontal=False,
    )

    if modo_add == "Repor bip devolvido (topo)":
        bip_manual = st.number_input(
            "Número do bip devolvido pelo cliente", min_value=1, step=1, value=1
        )
        if st.button("Empilhar bip devolvido", use_container_width=True):
            pilha.empilhar(int(bip_manual))
            st.success(f"Bip #{int(bip_manual)} foi devolvido e colocado no topo da torre.")
    else:
        if st.button("Adicionar novo bip sequencial", use_container_width=True):
            novo_bip = st.session_state.proximo_bip
            pilha.empilhar(novo_bip)
            st.session_state.proximo_bip += 1
            st.success(f"Bip #{novo_bip} foi cadastrado e colocado no topo da torre.")

# --------------------------- Visualização da torre --------------------------
with col_torre:
    st.subheader("Torre de bips (visão do topo para a base)")

    if pilha.esta_vazia():
        st.warning("A torre de bips está vazia.")
    else:
        bips_do_topo_para_base = pilha.como_lista()
        for i, bip in enumerate(bips_do_topo_para_base):
            if i == 0:
                st.markdown(
                    f"""
                    <div style="background-color:#FF4B4B;color:white;
                    padding:10px;border-radius:8px;margin-bottom:4px;
                    text-align:center;font-weight:bold;">
                    🔔 Bip #{bip}  ← TOPO (próximo a ser entregue)
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                    <div style="background-color:#31333F;color:white;
                    padding:8px;border-radius:6px;margin-bottom:4px;
                    text-align:center;opacity:{max(0.4, 1 - i * 0.05)};">
                    Bip #{bip}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

st.divider()

# --------------------------- Histórico de entregas ---------------------------
st.subheader("📋 Histórico de pedidos entregues")
if not st.session_state.historico:
    st.caption("Nenhum pedido entregue ainda.")
else:
    st.dataframe(
        [
            {"Pedido": e.pedido, "Bip entregue": e.bip, "Horário": e.horario}
            for e in st.session_state.historico
        ],
        use_container_width=True,
        hide_index=True,
    )
