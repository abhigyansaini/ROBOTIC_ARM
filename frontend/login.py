import streamlit as st
from api import login_user, register_user, check_api_status, BASE_URL


def show_login():
    # -----------------------------
    # Page styling
    # -----------------------------
    st.markdown(
        """
        <style>
        .login-hero {
            text-align: center;
            padding: 2rem 1rem 1rem 1rem;
        }
        .brand-badge {
            display: inline-block;
            background: linear-gradient(135deg, #0ea5e9, #0284c7);
            color: #ffffff;
            font-size: 13px;
            font-weight: 700;
            letter-spacing: 1.5px;
            text-transform: uppercase;
            padding: 6px 14px;
            border-radius: 9999px;
            margin-bottom: 12px;
            box-shadow: 0 4px 14px rgba(14, 165, 233, 0.35);
        }
        .brand-title {
            font-size: 38px;
            font-weight: 800;
            color: #0f172a;
            letter-spacing: -0.5px;
            margin: 0 0 8px 0;
        }
        .brand-subtitle {
            font-size: 16px;
            color: #64748b;
            margin-bottom: 25px;
        }
        .server-pill {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            font-size: 12px;
            padding: 4px 12px;
            border-radius: 6px;
            margin-bottom: 20px;
        }
        .server-online {
            background-color: #ecfdf5;
            color: #059669;
            border: 1px solid #a7f3d0;
        }
        .server-offline {
            background-color: #fef2f2;
            color: #dc2626;
            border: 1px solid #fecaca;
        }
        .demo-card {
            background: #f8fafc;
            border: 1px dashed #cbd5e1;
            border-radius: 10px;
            padding: 12px 16px;
            margin-top: 16px;
            font-size: 13px;
            color: #475569;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------
    # Check Backend Status
    # -----------------------------
    is_online = check_api_status()

    # -----------------------------
    # Header & Branding
    # -----------------------------
    col_center, _ = st.columns([1, 0.01])
    with col_center:
        st.markdown(
            f"""
            <div class="login-hero">
                <div class="brand-badge">⚡ Industrial IoT & AI Platform</div>
                <h1 class="brand-title">🤖 RoboPulse AI</h1>
                <p class="brand-subtitle">Predictive Intelligence & Multi-Axis Diagnostics for Industrial Robot Arms</p>
                <div class="server-pill {'server-online' if is_online else 'server-offline'}">
                    <span>{'🟢 API Connected' if is_online else '🔴 API Offline (Check Port 8000)'}</span>
                    <span>•</span>
                    <code>{BASE_URL}</code>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # -----------------------------
    # Auth Form Container
    # -----------------------------
    _, col_form, _ = st.columns([1, 2, 1])

    with col_form:
        tab_login, tab_register = st.tabs(["🔐 Operator Sign In", "📝 Create Account"])

        # -----------------------------
        # TAB 1: SIGN IN
        # -----------------------------
        with tab_login:
            with st.form("login_form"):
                st.markdown("##### Sign in to access your sector dashboard")
                email = st.text_input("Work Email", placeholder="operator@factoryops.com or admin@test.com")
                password = st.text_input("Password", type="password", placeholder="••••••••")

                submit_login = st.form_submit_button("Authenticate & Enter System", use_container_width=True)

                if submit_login:
                    if not email or not password:
                        st.warning("Please enter both email and password.")
                    else:
                        with st.spinner("Authenticating with FastAPI backend..."):
                            data, err = login_user(email, password)

                        if data and "access_token" in data:
                            st.session_state["logged_in"] = True
                            st.session_state["access_token"] = data["access_token"]
                            st.session_state["user_id"] = data.get("user_id")
                            st.session_state["full_name"] = data.get("full_name", "Operator")
                            st.session_state["email"] = data.get("email", email)
                            st.session_state["role"] = data.get("role", "Operator")

                            st.success(f"Authenticated as **{data.get('full_name')}** ({data.get('role')})")
                            st.rerun()
                        else:
                            st.error(f"Login failed: {err or 'Invalid credentials'}")

            # Quick credentials hint
            st.markdown(
                """
                <div class="demo-card">
                    <strong>💡 Demo Credentials:</strong><br>
                    • Admin: <code>admin@test.com</code> / <code>Admin@123</code><br>
                    • Operator / Seed user: <code>user1@factoryops.com</code> / <code>admin123</code>
                </div>
                """,
                unsafe_allow_html=True,
            )

        # -----------------------------
        # TAB 2: REGISTER
        # -----------------------------
        with tab_register:
            with st.form("register_form"):
                st.markdown("##### Register a new operator or supervisor profile")
                reg_name = st.text_input("Full Name", placeholder="e.g. John Doe")
                reg_email = st.text_input("Work Email", placeholder="e.g. j.doe@factoryops.com")
                reg_phone = st.text_input("Contact Phone (Optional)", placeholder="e.g. +1 555-0199")
                reg_pwd = st.text_input("Create Password", type="password", placeholder="••••••••")
                reg_confirm = st.text_input("Confirm Password", type="password", placeholder="••••••••")

                submit_register = st.form_submit_button("Create Operator Profile", use_container_width=True)

                if submit_register:
                    if not reg_name or not reg_email or not reg_pwd:
                        st.warning("Please fill in full name, email, and password.")
                    elif reg_pwd != reg_confirm:
                        st.error("Passwords do not match. Please re-enter.")
                    else:
                        with st.spinner("Registering user profile with backend..."):
                            reg_data, reg_err = register_user(
                                full_name=reg_name,
                                email=reg_email,
                                password=reg_pwd,
                                confirm_password=reg_confirm,
                                phone=reg_phone,
                            )

                        if reg_data:
                            st.success(f"Account created successfully for {reg_data.get('full_name')}! You can now switch to the 'Operator Sign In' tab to log in.")
                        else:
                            st.error(f"Registration failed: {reg_err or 'Unknown error'}")